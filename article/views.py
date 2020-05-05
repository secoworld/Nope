
from django.shortcuts import render, redirect, reverse, HttpResponse
import json
from .models import Article, Category, Tags, Carousel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core import serializers
from comment.models import Comment
from django.http import JsonResponse, response
from .forms import CommentForms
from django.db.models import Q
import markdown
from FriendLink.models import FriendLink
import requests
import time
import collections
import json
from django.core import serializers
# Create your views here.


# 通用的样式
def commont_get(request):
    list_category = [[], ]
    hot_articles = Article.objects.all().order_by('-id')[:5]
    categorys = Category.objects.all()
    first_category = Category.objects.filter(rank=1)
    second_category = Category.objects.filter(rank=2)
    carousal = Carousel.objects.filter(showFlag=True)
    if carousal:
        print(carousal[0].img)
    friendlink = FriendLink.objects.all()
    tags = Tags.objects.all()

    return locals()

def mark_contrct(objs):
    for obj in objs:
        obj.context = markdown.markdown(obj.context,extensions=[
            'markdown.extensions.extra',
            # 语法高亮扩展
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
       

# 获得评论
def getComment(obj):
    for art in obj:
        art.comment = art.comment_set.all()
    return obj


def setPage(request, lists, num):
    total = lists.count
    pages = Paginator(lists, num)
    page = request.GET.get('page')

    try:
        lists = pages.get_page(page)
    except EmptyPage:
        lists = pages.get_page(pages.num_pages)  # 返回最后一页
    except:
        lists = pages.get_page(1)  # 返回首页
    lists.count = total     #返回文章的总数
    return lists, pages


# 开始页面
def index(request):
    articles = Article.objects.all().order_by('-id')
    articles=getComment(articles)
    articles,pages = setPage(request, articles, 10)
    # mark_contrct(articles)
    return render(request, 'index.html', locals())


# 显示文章
def article_show(requset, aid):
    essay = Article.objects.get(id=aid)
    essay.views = essay.views + 1
    print("观看的人数为" + str(essay.views))
    essay.save()
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    essay.context = md.convert(essay.context)
    essay.toc = md.toc
    # 观看人数需要保存到数据中，不然每次都会是1
    
    comments = essay.comment_set.all().order_by('-created_time')


    for com in comments:
        com.context = markdown.markdown(com.context, extensions=[
                                     'markdown.extensions.extra',
                                    # 语法高亮扩展
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                     ])
    formtext = CommentForms()

    # comments = list(commentTree(comments));
    # print(comments)

    # 上一篇和下一篇文章
    pre_blog = Article.objects.filter(id__lt=aid).order_by('-id')
    next_blog = Article.objects.filter(id__gt=aid).order_by('id')

    if pre_blog.count() > 0:
        pre_blog = pre_blog[0]
    else:
        pre_blog = None

    if next_blog.count() > 0:
        next_blog = next_blog[0]
    else:
        next_blog = None

    if requset.method == 'POST':
        forms = CommentForms(requset.POST)
        if forms.is_valid:
            comment = forms.save(commit=False)
            comment.article = essay
            comment.user = requset.user
            comment.save()
            return redirect(reverse('article:detail', args=[aid, ]))

    return render(requset, 'detail.html', locals())



# 显示列表
def category_list(request, urlname):
    lists = Article.objects.filter(Q(category__urlname=urlname) | Q(
        category__father__urlname=urlname)).order_by('-id')

    try:
        list_name = Category.objects.get(urlname=urlname).name
    except:
        list_name = "你查找的分类为空"

    lists, pages = setPage(request, lists, 10)
    getComment(lists)
    # print(locals());

    return render(request, 'list.html', locals())

#使用json返回对象
def json_list(request, urlname):
    lists = Article.objects.filter(Q(category__urlname=urlname) | Q(
        category__father__urlname=urlname)).order_by('-id')
    # 处理QuerySet, 转化成为json
    # ret =  json.dumps(lists, ensure_ascii=False)
    try:
        list_name = Category.objects.get(urlname=urlname).name
    except:
        list_name = "你查找的分类为空"

    lists, pages = setPage(request, lists, 10)
    # getComment(lists)

    ret  = serializers.serialize("json", lists)
    return JsonResponse(ret, safe=False)

# 显示列表
def tag_list(request, tag):
    lists = Article.objects.filter(tags__name=tag).order_by('-id')

    try:
        list_name = tag
    except:
        list_name = "你查找的标签为空"

    lists, pages = setPage(request, lists, 10)
    getComment(lists)
    return render(request, 'list.html', locals())


# 查找
def Search(request):
    word = request.GET.get('search')
    print(request.GET)
    if not word:
        list_name = "未找到相关的内容"
        lists = ""
        return render(request, 'list.html', locals())

    lists = Article.objects.filter(
        Q(title__icontains=word) | Q(context__icontains=word)).order_by('-created_time')

    list_name = word
    print("lists=",lists)

    lists, pages = setPage(request, lists, 10)
    getComment(lists)

    return render(request, 'list.html', locals())


def update_comment(request):
    refer = request.META.get('HTTP_REFERER', reverse('article:home'))
    form = CommentForms(request.POST)
    data = {}

    if form.is_valid():
        aid = request.POST.get('aid')
        print("aid=", aid)
        comment = Comment()
        # comment = Us
        comment.name = form.cleaned_data['name']
        comment.email = form.cleaned_data['email']
        comment.article = Article.objects.get(id=aid)
        comment.context = form.cleaned_data['context']
        parent_id = form.cleaned_data['parent_id']
        if parent_id != -1:
            comment.parent = Comment.objects.get(id=parent_id)
        comment.save()

        # 返回的参数
        data['status'] = 'success'
        data['username'] = request.user.username
        data['comment_time'] = comment.created_time.strftime('%Y-%m-%d %H-%M-%S')
        data['text'] = comment.context
        data['commnet_id'] = comment.id
        print(data)
    else:
        data['status'] = 'Error'
        data['message'] = list(form.errors.values())[0][0]

        # 以Json的形式返回数据
    return JsonResponse(data)


def urls_push():
    url = 'http://data.zz.baidu.com/urls?site=https://www.liulongtao.com&token=kHA6zh1nAq4xtHkW'
    base_url = 'https://www.liulongtao.com/article/'
    header = {
    'User-Agent': 'curl/7.12.1' ,
    'Host': 'data.zz.baidu.com' ,
    'Content-Type': 'text/plain' ,
    'Content-Length': '83',
    }
    articles = Article.objects.all()
    data =[]
    for art in articles:
        data.append(base_url+str(art.id))

    # 将data数据转换为文本样式
    data = '\n'.join(data)
    req  = requests.post(url, data = data, headers = header)
    print(time.asctime(time.localtime()), end=' : ')
    print(req.json())

    return req.json()


# 设置新建一个将comment结构化的函数
def commentTree(aid):
    comments = Comment.objects.filter(article_id=aid)
    comment_parent = comments.filter(parent__isnull=True).order_by('-id').values()
    comments_list = []
    # for comment in comments:
    #     comment['childrens'] = []
    comments_list = setCommentTree(comment_parent, comments)
    return comments_list

# 对comment进行结构化
def setCommentTree(comments_parent, comments):
    for comment in comments_parent:
        comment_patent_id = comment['id']
        if comment_patent_id is None:
            continue
        childrens = comments.filter(parent_id=comment_patent_id).values()
        if len(childrens) == 0:
            continue
        childrens = setCommentTree(childrens, comments)
        comment['childrens'] = list(childrens)
    return comments_parent


# 对评论进行整理
# def CommnetTree(comments):
#     # 首先建立一个顺序的字典，然后判断是否存在父级评论，如果存在父级评论的话，
#     # 就将评论加入到字典中
#     comment_tree = collections.OrderedDict()
#
#     for comment in comments:
#         if comment.parent is None:
#             # 如果是根评论，那么将设为空得子集
#             comment_tree[comment] = collections.OrderedDict()
#         else:
#             # 如果不是根评论，那么寻找相关的父级
#             CommentSearch(comment_tree, comment)
#     return comment_tree
#
# # 在字典中寻找相关的父级评论
# def CommentSearch(comment_tree, comment):
#     # 在字典中一个接一个的寻找相关的字典
#     for key,value  in comment_tree.items():
#         # 如果找到评论，那么将自己存入到字典中
#         if key[0] == comment_tree[comment]:
#             comment_tree[key][comment] = collections.OrderedDict()
#             return
#         else:
#             # 在当前第一个递归中寻找父节点
#             CommentSearch(comment_tree[key], comment)
#

# 获取comments
# 获取评论
def get_comments(request, aid):
    data = {}
    data['comment'] = list(commentTree(aid))
    print(data)
    return JsonResponse(data, safe=False)
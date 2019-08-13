from django.shortcuts import render, redirect, reverse
from .models import Article, Category, Tags
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from comment.models import Comment
from django.http import JsonResponse
from .forms import CommentForms
from django.db.models import Q
import markdown
# Create your views here.

# 通用的样式


def commont_get(request):
    list_category = [[], ]
    hot_articles = Article.objects.all().order_by('-id')[:5]
    categorys = Category.objects.all()
    first_category = Category.objects.filter(rank=1)
    second_category = Category.objects.filter(rank=2)
    tags = Tags.objects.all()

    return locals()


def setPage(request, lists, num):
    paginator = Paginator(lists, num)
    page = request.GET.get('page')

    try:
        lists = paginator.get_page(page)
    except EmptyPage:
        lists = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        lists = paginator.get_page(1)  # 返回首页

    return lists

# 开始页面


def index(request):
    articles = Article.objects.all().order_by('-id')

    # setPage(request, articles, 5)
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')

    try:
        articles = paginator.get_page(page)
    except EmptyPage:
        articles = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        articles = paginator.get_page(1)  # 返回首页

    return render(request, 'index.html', locals())


# 显示文章
def article_show(requset, aid):
    essay = Article.objects.get(id=aid)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    essay.context = md.convert(essay.context)
    essay.toc = md.toc
    essay.views += 1
    comments = essay.comment_set.all().order_by('-created_time')
    for com in comments:
        com.context = markdown.markdown(com.context, extensions=[
                                     'markdown.extensions.extra',
                                    # 语法高亮扩展
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                     ])
    formtext = CommentForms()

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
    paginator = Paginator(lists, 10)
    page = request.GET.get('page')

    try:
        lists = paginator.get_page(page)
    except EmptyPage:
        lists = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        lists = paginator.get_page(1)  # 返回首页

    return render(request, 'list.html', locals())


# 显示列表
def tag_list(request, tag):
    lists = Article.objects.filter(tags__name=tag).order_by('-id')

    try:
        list_name = tag
    except:
        list_name = "你查找的标签为空"

    paginator = Paginator(lists, 10)
    page = request.GET.get('page')

    try:
        lists = paginator.get_page(page)
    except EmptyPage:
        lists = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        lists = paginator.get_page(1)  # 返回首页

    return render(request, 'list.html', locals())

# 查找


def Search(request):
    word = request.GET.get('search')

    if not word:
        list_name = "未找到相关的内容"
        lists = ""
        return render(request, 'list.html', locals())

    lists = Article.objects.filter(
        Q(title__icontains=word) | Q(context__icontains=word))

    list_name = word
    paginator = Paginator(lists, 10)
    page = request.GET.get('page')

    try:
        lists = paginator.get_page(page)
    except EmptyPage:
        lists = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        lists = paginator.get_page(1)  # 返回首页

    return render(request, 'list.html', locals())


def update_comment(request):
    refer = request.META.get('HTTP_REFERER', reverse('article:home'))
    form = CommentForms(request.POST)
    data = {}

    if form.is_valid():
        comment = Comment()
        # comment = Us
        comment.user = request.user
        comment.context = form.cleaned_data['context']
        comment.save()

        # 返回的参数
        data['status'] = 'success'
        data['username'] = request.user.username
        data['comment_time'] = comment.created_time.strftime('%Y-%m-%d %H-%M-%s')
        data['text'] = comment.context
    else:
        data['status'] = 'Error'
        data['message'] = list(form.errors.values())[0][0]

        # 以Json的形式返回数据
    return JsonResponse(data)

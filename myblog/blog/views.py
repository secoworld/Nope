from django.shortcuts import render
from django.http import HttpResponse
from .models import  Article,Tags,Category
from django.core.paginator import Paginator
from comment.models import Comment
# 搜索引擎
from django.db.models import Q
#引入markdown 语法
import markdown

# Create your views here.

# 将重复的内容进行整理
def get_context(request):
    # 所有的标签
    tags = Tags.objects.all()
    # 右侧推荐文章
    right_articles = Article.objects.all().order_by('-id')[:5]
    # 分类
    categorys = Category.objects.all()
    # 
    return locals()


def test(request):
    context  = {}
    return render(request, "base.html", context)


# 设置首页
def index(request):
    articles = Article.objects.all().order_by('-id')
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    list_article = paginator.get_page(page)

    return render(request, "index.html", locals())

# 设置文章页
def detail(request, aid):
    article = Article.objects.get(id=aid)
    #使用Markdown语法进行渲染
    article.body =  markdown.markdown(article.content,
                                  extensions=[
                                    #   包含缩写、表格等常用的拓展
                                     'markdown.extensions.extra',
                                    #  语法高亮
                                     'markdown.extensions.codehilite',
                                    #  'markdown.extensions.toc',
                                  ])
    article.views += 1
    # 提取评论
    comments = Comment.objects.filter(article_id=aid)
    # 设置文章的相关文章
    # last_article = Article.objects.filter(id__lt=aid).order_by('-id').first()
    # next_article = Article.objects.filter(id__gt=aid).order_by('id').first()

    # return render(request, "detail.html", locals())
    return render(request, 'detail.html', locals())

#设置分类列表页
def category_list(request, url_name):
    #分类对应的文章列表
    list_article = Article.objects.filter(category__url_name= url_name).order_by('-id')
    list_name = Category.objects.get(url_name=url_name).name
    paginator = Paginator(list_article, 5)     #每页显示10个
    page = request.GET.get('page')  #获取当前页面的页码

    #进行页面处理
    try:
        list_article = paginator.get_page(page)
    except EmptyPage:
        list_article = paginator.page(paginator.num_pages)   #返回最后一页 
    except PagNotAnInteger:
        list_article = paginator.page(1)  #返回首页

    return render(request, "list.html",  locals())


# 设置标签页
def tag(request, tag):
    # 标签含有tag的文章
    article = Article.objects.filter(tags__name = tag)
    #分类对应的文章列表
    list_article = Article.objects.filter(tags__name = tag).order_by('-id')
    list_name = tag
    #设置分页
    paginator = Paginator(list_article, 5)
    page = request.GET.get('page')
    list_article = paginator.get_page(page)

    return render(request, "list.html", locals())

    
def Search(request):
    # 查询关键字
    search = request.GET.get('search')
    error_msg = "查找错误"

    if not search:
        list_name = "没有找到相关内容：" + search
        list_article = ""
        return render(request, "list.html", locals())
    list_article =  Article.objects.filter(Q(title__icontains=search)| Q(content__icontains=search))

    list_name = search
    #设置分页
    paginator = Paginator(list_article, 5)
    page = request.GET.get('page')
    list_article = paginator.get_page(page)

    return render(request, "list.html", locals())


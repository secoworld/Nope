from django.shortcuts import render
from django.http import HttpResponse
from .models import  Article,Tags,Category
from django.core.paginator import Paginator
#引入markdown 语法
import markdown

# Create your views here.
def test(request):
    context  = {}
    return render(request, "base.html", context)


# 设置首页
def index(request):
    articles = Article.objects.all().order_by('-id')
    right_articles = Article.objects.all().order_by('-id')[:5]
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    list_article = paginator.get_page(page)

    return render(request, "index.html", locals())

# 设置文章页
def detail(request, aid):
    right_articles = Article.objects.all().order_by('-id')[:5]
    article = Article.objects.get(id=aid)
    #使用Markdown语法进行渲染
    article.content =  markdown.markdown(article.content,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    article.views += 1

    return render(request, "detail.html", locals())

#设置分类列表页
def category_list(request, category_name):
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    #右侧显示的文章
    right_articles = Article.objects.all().order_by('-id')[:5]
    #分类对应的文章列表
    list_article = Article.objects.filter(category__name= category_name).order_by('-id')
    list_name = category_name
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
    tags = Tags.objects.all()
    categorys = Category.objects.all()
    #右侧显示的文章
    right_articles = Article.objects.all().order_by('-id')[:5]
    #分类对应的文章列表
    list_article = Article.objects.filter(tags__name = tag).order_by('-id')
    list_name = tag
    #设置分页
    paginator = Paginator(list_article, 5)
    page = request.GET.get('page')
    list_article = paginator.get_page(page)

    return render(request, "list.html", locals())

    

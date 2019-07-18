from django.shortcuts import render
from .models import Article, Category, Tags
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from comment.models import Comment
# Create your views here.

# 通用的样式
def commont_get(request):
    hot_articles = Article.objects.all().order_by('-id')[:5]
    categorys = Category.objects.all()
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
        lists = paginator.get_page(1)    #返回首页

    return lists

# 开始页面
def index(request):
    articles = Article.objects.all()
    
    # setPage(request, articles, 5)
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')

    try:
        articles = paginator.get_page(page)
    except EmptyPage:
        articles = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        articles = paginator.get_page(1)    #返回首页

    return render(request, 'index.html', locals())



# 显示文章
def article_show(requset, aid):
    essay = Article.objects.get(id=aid)
    comments = Comment.objects.filter(article__id=aid)

    return render(requset, 'detail.html', locals())

# 显示列表
def category_list(request, urlname):
    lists = Article.objects.filter(category__urlname=urlname)
    paginator = Paginator(lists, 10)
    page = request.GET.get('page')

    try:
        lists = paginator.get_page(page)
    except EmptyPage:
        lists = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        lists = paginator.get_page(1)    #返回首页

    return render(request, 'list.html', locals())



# 显示列表
def tag_list(request, tag):
    lists = Article.objects.filter(tags__name = tag)
    paginator = Paginator(lists, 10)
    page = request.GET.get('page')

    try:
        lists = paginator.get_page(page)
    except EmptyPage:
        lists = paginator.get_page(paginator.num_pages)  # 返回最后一页
    except:
        lists = paginator.get_page(1)    #返回首页

    return render(request, 'list.html', locals())
from django.shortcuts import render
from .models import Article, Category, Tags
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from comment.models import Comment
# Create your views here.

# 通用的样式
def commont_get(request):
    hot_articles = Article.objects.all().order_by('-id')
    categorys = Category.objects.all()
    tags = Tags.objects.all()

    return locals()

def setPage(request, lists, num):
    paginator = Paginator(list, num)
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
def article_show(requset, id):
    aritcle = Article.objects.get(id=id)
    comments = Comment.objects.filter(article__id=id)

    return render(request, 'detail.html', locals())

# 显示列表
def category_list(request, urlname):
    lists = Category.objcts.filter(urlname=urlname)
    setPage(request, lists, 10)
    return render(request, 'list.html', locals())



# 显示列表
def tag_list(request, tag):
    lists = Tags.objcts.filter(name=tag)
    setPage(request, lists, 10)

    return render(request, 'list.html', locals())
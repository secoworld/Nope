from django.shortcuts import render
from .models import Category,Banner,Article,Tags,Tui,Link
#引入分页的模块
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
#开始页
def index(request):
    """
    设置blog的初始页面
    :param request: 请求
    :return:
    """
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(isactive=True)[0:4]     #对幻灯片进行处理
    tui = Article.objects.filter(tui__id=1)[:3]
    article = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[0:10]     #通过浏览数进行排序
    links = Link.objects.all()      #友链
    remen = Article.objects.filter(tui__id=2)[:6]          #右侧推荐列表
    tags = Tags.objects.all()
    context = {
        'allcategory' : allcategory,
        'banner': banner,
        'tui':tui,
        'article' : article,
        'hot':hot,
        'links':links,
        'remen':remen,
        'tags':tags,
    }
    return render(request, 'index.html',context)

#标签页
def tags(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 获取传进来的tag名称
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐栏
    allcategory = Category.objects.all()  # 获取全全部的分类
    tname = Tags.objects.get(name=tag)      #获取当前的标签的名称
    page = request.GET.get('page')
    tags = Tags.objects.all()
    paginator = Paginator(list, 5)  #每一页5p篇文章
    try:
        list = paginator.page(page)     #获取当前的页码
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  #如果用户输入的页码数超过当前的页码域，返回最后的一页
    except PageNotAnInteger:
        list = paginator.page(1)    #如果用户输入的不是正数，则进入第一页
    return render(request, 'tags.html', locals())


#列表页
def list(request, lid):
    list = Article.objects.filter(category_id=lid)      #获取传进来的lid
    cname = Category.objects.get(id=lid)        #获取当前文章的栏目名
    remen = Article.objects.filter(tui__id=2)[:6]   #右侧热门推荐栏
    allcategory = Category.objects.all()    #获取全全部的分类
    tags = Tags.objects.all()       #获取全部的标签

    #对列表进行分页
    page  = request.GET.get('page')       #在URL中获取page页码
    paginator = Paginator(list, 5)      #超过5条就进行分页
    try:
        list = paginator.page(page)     #获取当前的页码
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  #如果用户输入的页码数超过当前的页码域，返回最后的一页
    except PageNotAnInteger:
        list = paginator.page(1)    #如果用户输入的不是正数，则进入第一页

    return render(request, 'list.html', locals())       #locals()是包含当前作用域的全部变量


#搜索页
def search(request):
    ss = request.GET.get('search')  #获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  #通过关键词进行检索
    cname = ss
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐栏
    allcategory = Category.objects.all()  # 获取全全部的分类
    tags = Tags.objects.all()  # 获取全部的标签

    # 对列表进行分页
    page = request.GET.get('page')  # 在URL中获取page页码
    paginator = Paginator(list, 5)  # 超过5条就进行分页
    try:
        list = paginator.page(page)  # 获取当前的页码
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页码数超过当前的页码域，返回最后的一页
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的不是正数，则进入第一页

    return render(request, 'list.html', locals())  # locals()是包含当前作用域的全部变量

#内容页
def show(request, sid):
    #我们需要获取，ID为sid的文章、导航上的分类、推荐文章、tags、热度文章、之前的文章、下一篇文章
    article = Article.objects.get(id=sid)
    tags = Tags.objects.all()
    hot = Article.objects.all().order_by('?')[:10]   #随机获取推荐的文章,放在内容的下边
    remen = Article.objects.filter(tui__id=2)[:6]       #右侧栏推荐文章
    prevous_blog = Article.objects.filter(created_time__gt=article.created_time, category=article.category).first()
    next_blog = Article.objects.filter(created_time__lt=article.created_time, category=article.category).last()
    article.views += 1
    article.save()
    return render(request, 'show.html', locals())


#关于我们
def aboutme(request):
    pass
from django.contrib import admin
from .models import Article,Banner,Tags,Tui,Category,Link



# Register your models here.
#对数据在Admin中进行登记
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 进行显示的内容
    list_display = ('id', 'name', 'index')

#推荐
@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#标签
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

#文章
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 进行显示的内容和顺序
    list_display = ('id','title', 'user','category', 'tui', 'views', 'created_time')
    #每页显示的内容的条数
    list_per_page = 50
    #后台的排序
    ordering = ('-created_time',)
    #设置一些链接点击即可进入编辑页面
    list_display_link = ('id', 'title')

#友链
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')

#幻灯片
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'isactive', 'img', 'link_url')
    

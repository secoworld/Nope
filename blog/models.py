from django.db import models
from django.contrib.auth.models import User
#导入富文本类型
from DjangoUeditor.models import UEditorField
# Create your models here.
#我们需要创建的数据类型表单为：文章分类、文章、文章标签、幻灯图、推荐位、友情链接

#文章分类
class Category(models.Model):
    name = models.CharField('博客分类',max_length=100)
    index = models.IntegerField(default=999, verbose_name="分类排序")

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#文章标签
class Tags(models.Model):
    name = models.CharField('文章标签', max_length=100)
    class Meta:
        verbose_name = "文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#推荐表
class Tui(models.Model):
    name = models.CharField("推荐", max_length=100)
    class Meta:
        verbose_name = "推荐"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#文章
class Article(models.Model):
    title = models.CharField('标题', max_length=100)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    #一对多的关系,分类表
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="分类", blank=True, null=True)
    #标签,标签是多个对多个的关系
    tags = models.ManyToManyField(Tags, verbose_name="标签", blank=True)
    #图片
    img = models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name="文章图片", blank=True, null=True)
    #文章内容
    #body = models.TextField()
    #将body的内容替换为富文本样式
    body = UEditorField('内容', width=800, height=500, toolbars='full', imagePath='upimg', filePath='upfile/',\
                        upload_settings={"imageMaxSize" : 1024000 }, settings={}, command=None, blank=True )
    user = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    #阅读量
    views = models.PositiveIntegerField('阅读量', default=0)
    #推荐位
    tui = models.ForeignKey(Tui, verbose_name="推荐位", on_delete=models.DO_NOTHING, blank=True, null=True)
    #文章创建的额时间和更改的时间
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    modified_time = models.DateTimeField("更改时间", auto_now=True)

    class Meta:
        verbose_name="文章"
        verbose_name_plural= verbose_name

    def __str__(self):
        return self.title
#幻灯片
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('链接', max_length=100)
    isactive = models.BooleanField('是否是active', default=False)

    class Meta:
        verbose_name = '幻灯片'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.text_info

#友链
class Link(models.Model):
    name = models.CharField('链接名称',  max_length=100)
    linkurl = models.URLField('网址', max_length=100)

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

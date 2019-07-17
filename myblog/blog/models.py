from django.db import models
#导入作者
from django.contrib.auth.models import User
# 尝试使用django-mdeditor
from mdeditor.fields import MDTextField

# Create your models here.
#定义数据模型

# 标签
class Tags(models.Model):
    name = models.CharField('标签名', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

# 分类
class Category(models.Model):
    def getUrlName(self):
        return self.name

    name = models.CharField("博客分类", max_length=100)
    # 别名，使用在网站栏中的内容
    url_name = models.CharField("url名称", max_length=50, blank=True, default=(name) )
    index = models.IntegerField(default=1, verbose_name="排序")
    
    def __str__(self):
        return self.name

    


    class Meta:
        verbose_name  = "博客分类"
        verbose_name_plural = verbose_name

# 文章
class Article(models.Model):
    #标题
    title = models.CharField("标题", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="分类",blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    #excerpt =  models.TextField("摘要", max_length=200, blank=True)
    # content = models.TextField("文章内容")
    # 尝试使用django-mdeditor
    content = MDTextField()
    tags  =  models.ManyToManyField(Tags, verbose_name="标签", blank=True)
    views = models.IntegerField("阅读量", default=0)
    #图片
    img = models.ImageField(upload_to="article_img/%Y/%m/%d/", verbose_name="图片", blank=True, null=True)
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    modified_time = models.DateTimeField("修改时间", auto_now=True)
    
    def _str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name



# 推荐文章
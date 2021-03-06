from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from mdeditor.fields import MDTextField
# Create your models here.
# 创建models规定article的属性
from ckeditor.fields import RichTextField

# 分类
class Category(models.Model):
    
    name = models.CharField("分类名", max_length=50)
    father = models.ForeignKey("self", verbose_name="父级", on_delete=models.DO_NOTHING, null=True, blank=True)
    rank = models.IntegerField("分类等级", default=1)
    show = models.BooleanField("列表显示", default=True)
    urlname = models.CharField("url名称", max_length=50, default="all")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 标签
class Tags(models.Model):
    
    name = models.CharField("标签名称", max_length=100)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签 "

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    
    title = models.CharField("标题", max_length=50)

    # context = models.TextField("文章内容")
    # 富文本编辑器
    context = MDTextField("文章内容")
    author = models.ForeignKey(User, verbose_name="作者", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tags, verbose_name="标签")
    created_time = models.DateTimeField("创建时间", auto_now=False, auto_now_add=True)
    modefid_time = models.DateTimeField("修改时间", auto_now=True, auto_now_add=False)
    views = models.IntegerField("观看人数", default=0)
    img = models.ImageField("图片", upload_to="article/%Y/%m/%d/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    # 增加评论
    # comment = models.OneToManyField()
    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "全部文章"

    def __str__(self):
        return self.title

# 设置轮播图
class Carousel(models.Model):
    name = models.CharField("图片名称", max_length=50)
    title = models.CharField("标题", max_length=100, null=True, blank=True)
    context = models.CharField("简介", max_length=200, null=True, blank=True)
    img = models.ImageField("展示的图片", upload_to="carousel/%Y/%m/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    showFlag = models.BooleanField("设置是否显示", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = "全部轮播图"

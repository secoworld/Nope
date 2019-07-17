from django.db import models
from django.contrib.auth.models import User
from blog.models import Article
# 引入django-mptt 模块
from mptt.models import MPTTModel, TreeForeignKey
# django-ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
# 提交平评论
# 将models.Model替换为MPTTModel
class Comment(MPTTModel):
    # 新增mptt树形结构
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    # 新增记录二级评论回复给谁
    reply_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="replyers")

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments", verbose_name="文章")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", verbose_name="用户")
    # body = models.TextField(verbose_name="评论内容")
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="评论时间")

    # class Meta:
    #     ordering = ('-created',)
    class MPTTMeta:
        order_insertion_by = ['-created']

    def __str__(self):
        return self.body[:20]
    
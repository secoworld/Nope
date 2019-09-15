from django.db import models
from django.contrib.auth.models import User
from article.models import Article
# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name="文章", on_delete=models.CASCADE)
    parent = models.ForeignKey("self", verbose_name="父级评论", on_delete=models.CASCADE, blank=True, null=True)
    rank = models.IntegerField("评论级数", default=1)
    context = models.TextField("评论的内容")
    user = models.ForeignKey(User, verbose_name="评论人", on_delete=models.CASCADE)
    created_time = models.DateTimeField("创建的时间", auto_now=False, auto_now_add=True)
    modfied_time = models.DateTimeField("修改时间", auto_now=True, auto_now_add=False)

    class Meta():
        verbose_name = "评论"
        verbose_name_plural = "全部评论"

    def __str__(self):
        return self.context

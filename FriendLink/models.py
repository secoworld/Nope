from django.db import models

# Create your models here.
class FriendLink(models.Model):
    name = models.CharField("友链名称", max_length=100)
    url = models.URLField("网站")
    create_time = models.DateTimeField("增加时间", auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "友链"
        verbose_name_plural = "友链"

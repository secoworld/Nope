from django.db import models
from django.contrib.auth.models import User
# 引入内置信号
from django.db.models.signals import post_save
# 引入信号接收器
from django.dispatch import receiver

# Create your models here.

# 用户信息拓展
class Profile(models.Model):
    # 与User模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # 电话字段
    phone = models.CharField(max_length=20, blank=True)
    # 头像
    avator = models.ImageField(upload_to="avator/%Y%m%d", blank=True)
    # 个人简历
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)

# 信号接收函数，每当新建User实例的时候，自动调用
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# 信号接收函数，每当更新User时候自动调用
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
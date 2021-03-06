# Generated by Django 2.2.3 on 2019-08-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_category_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='图片名称')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('context', models.CharField(max_length=200, verbose_name='简介')),
                ('img', models.ImageField(blank=True, null=True, upload_to='carousel/', verbose_name='展示的图片')),
                ('showFlag', models.BooleanField(default=False, verbose_name='设置是否显示')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '全部轮播图',
            },
        ),
    ]

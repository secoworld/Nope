# Generated by Django 2.2.1 on 2019-06-10 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_category_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url_name',
            field=models.CharField(blank=True, default=models.CharField(max_length=100, verbose_name='博客分类'), max_length=50, verbose_name='url名称'),
        ),
    ]

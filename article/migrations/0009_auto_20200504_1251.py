# Generated by Django 2.2.3 on 2020-05-04 04:51

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20200504_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='context',
            field=mdeditor.fields.MDTextField(verbose_name='文章内容'),
        ),
    ]

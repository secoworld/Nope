# Generated by Django 2.2.3 on 2020-05-04 02:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190824_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='context',
            field=ckeditor.fields.RichTextField(verbose_name='文章内容'),
        ),
    ]

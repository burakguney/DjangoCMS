# Generated by Django 3.2 on 2021-04-30 13:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(help_text='Maksimum 50 karakter, benzersiz.', max_length=100, unique=True, verbose_name='Blog Başlığı')),
                ('blogContent', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Blog İçeriği')),
                ('blogDate', models.DateTimeField(auto_now=True, verbose_name='Blog Tarihi')),
                ('blogImage', models.ImageField(default='blog/default_blog_image.png', help_text='600x600 piksel olmalı.', upload_to='blog/tr/%Y/%m/%d/', verbose_name='Blog Görseli')),
                ('blogSlug', models.SlugField(help_text='Blog başlığının url uzantı formatı, benzersiz.', max_length=100, unique=True, verbose_name='Blog Uzantısı')),
            ],
            options={
                'verbose_name': 'Blog Yazısı',
                'verbose_name_plural': 'Blog Yazıları',
            },
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP Adresi')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Son Görülme Tarihi')),
                ('blog', models.ManyToManyField(to='iknowcms_blog.Blog')),
            ],
            options={
                'verbose_name': 'IP Adresi',
                'verbose_name_plural': 'IP Adresleri',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='blog_views', to='iknowcms_blog.IpModel'),
        ),
    ]
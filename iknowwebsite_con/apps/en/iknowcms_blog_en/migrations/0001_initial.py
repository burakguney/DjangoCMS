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
                ('blogTitle', models.CharField(help_text='Maximum 100 character, unique.', max_length=100, unique=True, verbose_name='Blog Title')),
                ('blogContent', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Blog Content')),
                ('blogDate', models.DateTimeField(auto_now=True, verbose_name='Blog Date')),
                ('blogImage', models.ImageField(default='blog/default_blog_image.png', help_text='Should be 600x600 pixels.', upload_to='blog/en/%Y/%m/%d/', verbose_name='Blog Image')),
                ('blogSlug', models.SlugField(help_text='Url format of the Blog Title, unique.', max_length=100, unique=True, verbose_name='Blog Slug')),
            ],
            options={
                'verbose_name': 'Blog Content',
                'verbose_name_plural': 'Blog Contents',
            },
        ),
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP Adresi')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Giriş Tarihi')),
                ('blog', models.ManyToManyField(to='iknowcms_blog_en.Blog')),
            ],
            options={
                'verbose_name': 'IP Address',
                'verbose_name_plural': 'IP Addresses',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='blog_views', to='iknowcms_blog_en.IpModel'),
        ),
    ]
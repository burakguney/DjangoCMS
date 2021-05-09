from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class IpModel(models.Model):
    ip = models.CharField(max_length=100, verbose_name="IP Adresi")
    blog = models.ManyToManyField('Blog')
    modified = models.DateTimeField(
        auto_now=True, verbose_name="Tarih")

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'IP Adresi'
        verbose_name_plural = 'IP Adresleri'


class Blog(models.Model):
    blogTitle = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Blog Başlığı",
        help_text="Maksimum 50 karakter, benzersiz.")

    blogContent = RichTextUploadingField(
        verbose_name="Blog İçeriği")

    blogDate = models.DateTimeField(
        auto_now=True,
        verbose_name="Blog Tarihi")

    blogImage = models.ImageField(
        upload_to="blog/tr/%Y/%m/%d/",
        default="blog/default_blog_image.png",
        verbose_name="Blog Görseli",
        help_text="600x400 piksel olmalı.")

    blogSlug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Blog Uzantısı",
        help_text="Blog başlığının url uzantı formatı, benzersiz.")

    views = models.ManyToManyField(
        IpModel, related_name="blog_views", blank=True)

    def __str__(self):
        return self.blogTitle

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Blog Yazısı'
        verbose_name_plural = 'Blog Yazıları'

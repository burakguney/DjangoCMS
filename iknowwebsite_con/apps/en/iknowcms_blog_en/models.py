from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class IpModel(models.Model):
    ip = models.CharField(max_length=100, verbose_name="IP Address")
    blog = models.ManyToManyField('Blog')
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date")

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'IP Address'
        verbose_name_plural = 'IP Addresses'


class Blog(models.Model):
    blogTitle = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Blog Title",
        help_text="Maximum 100 character, unique.")

    blogContent = RichTextUploadingField(
        verbose_name="Blog Content")

    blogDate = models.DateTimeField(
        auto_now=True,
        verbose_name="Blog Date")

    blogImage = models.ImageField(
        upload_to="blog/en/%Y/%m/%d/",
        default="blog/default_blog_image.png",
        verbose_name="Blog Image",
        help_text="Should be 600x400 pixels.")

    blogSlug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Blog Slug",
        help_text="Url format of the Blog Title, unique.")

    views = models.ManyToManyField(
        IpModel, related_name="blog_views", blank=True)

    def __str__(self):
        return self.blogTitle

    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Blog Content'
        verbose_name_plural = 'Blog Contents'

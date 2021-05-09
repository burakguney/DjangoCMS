from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Portfolio(models.Model):
    portfolioTitle = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Proje Başlığı",
        help_text="Maksimum 100 karakter, benzersiz.")

    portfolioContent = RichTextUploadingField(
        verbose_name="Proje İçeriği")

    portfolioImage = models.ImageField(
        upload_to="project/tr/%Y/%m/%d/",
        default="project/default_project_image.png",
        verbose_name="Proje Görseli",
        help_text="600x400 piksel olmalı.")

    portfolioSlug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Proje Uzantısı",
        help_text="Proje başlığının url uzantı formatı, benzersiz.")

    def __str__(self):
        return self.portfolioTitle

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

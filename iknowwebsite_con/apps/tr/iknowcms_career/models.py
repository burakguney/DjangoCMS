from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Career(models.Model):
    careerTitle = models.CharField(
        max_length=50,
        verbose_name="İş İlanı Başlığı")

    careerContent = RichTextField(
        verbose_name="İş İlanı İçeriği")

    careerDate = models.DateTimeField(auto_now_add=True)

    careerLocation = models.CharField(
        max_length=50,
        verbose_name="İş İlanı Lokasyonu",
        default="Türkiye/Edirne")

    careerSlug = models.SlugField(
        unique=True,
        verbose_name="İş İlanı Uzantısı",
        help_text="İlan Başlığı + İlan Tarihi url uzantı formatı, benzersiz.")

    def __str__(self):
        return self.careerTitle

    class Meta:
        verbose_name = 'İş İlanı'
        verbose_name_plural = 'İş İlanları'

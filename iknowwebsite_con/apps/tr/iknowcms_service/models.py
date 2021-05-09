from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Service(models.Model):
    serviceTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Hizmet Başlığı",
        help_text="Maksimum 50 karakter, benzersiz.")

    serviceContent = RichTextField(
        verbose_name="Hizmet İçeriği")

    serviceIcon = models.CharField(
        max_length=50,
        default='<i class="fas fa-server fa-5x"></i>',
        verbose_name="Hizmet İkon",
        help_text="Buraya Font Awesome'dan uygun bir ikonun etiketini yapıştırın. İkon boyutu için classın sonuna fa-2x, fa-3x, fa-5x eklenebilir.")

    serviceSlug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Hizmet Uzantısı",
        help_text="Hizmet başlığının url uzantı formatı, benzersiz.")

    def __str__(self):
        return self.serviceTitle

    class Meta:
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'

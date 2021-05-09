from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Carousel(models.Model):
    carouselTitle = models.CharField(
        unique=True,
        max_length=50,
        verbose_name="Görsel Başlığı",
        help_text="Maksimum 50 karakter. Görsel içerisinde yer alan yazıdan bir kesit.")

    carouselImageLarge = models.ImageField(
        upload_to="carousel/tr/large/",
        default="carousel/large/default_carouselLarge_image.png",
        verbose_name="Büyük Görsel",
        help_text="1200x400 piksel olmalı.")

    carouselImageMedium = models.ImageField(
        upload_to="carousel/tr/medium/",
        default="carousel/medium/default_carouselMedium_image.png",
        verbose_name="Orta Büyüklük Görsel",
        help_text="720x400 piksel olmalı.")

    carouselImageSmall = models.ImageField(
        upload_to="carousel/tr/small/",
        default="carousel/small/default_carouselSmall_image.png",
        verbose_name="Küçük Görsel",
        help_text="575x575 piksel olmalı.")

    carouselContent = RichTextUploadingField(
        verbose_name="Görsel İçeriği")

    carouselBackgroundColor = models.CharField(
        max_length=20,
        verbose_name="Arka Plan Rengi",
        help_text="Örnek: #ffbd59",
        default="#ffbd59")

    carouselSlug = models.SlugField(
        unique=True,
        max_length=50,
        verbose_name="Görsel Uzantısı",
        help_text="Görsel başlığının url uzantı formatı, benzersiz.",)

    def __str__(self):
        return self.carouselTitle

    class Meta:
        verbose_name = 'Anasayfa Görseli'
        verbose_name_plural = 'Anasayfa Görselleri'


class Testimonial(models.Model):
    testimonialTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Referans Başlığı",
        help_text="Maksimum 50 karakter, benzersiz.")

    testimonialContent = models.TextField(
        verbose_name="Referans İçeriği")

    testimonialImage = models.ImageField(
        upload_to="testimonial/tr/",
        default="testimonial/default_testimonial_image.svg",
        verbose_name="Referans Görseli")

    def __str__(self):
        return self.testimonialTitle

    class Meta:
        verbose_name = 'Referans'
        verbose_name_plural = 'Referanslar'


class Client(models.Model):
    clientTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Şirket Adı",
        help_text="Maksimum 50 karakter, benzersiz.")

    clientImage = models.ImageField(
        upload_to="client/tr/",
        default="client/default_client_image.svg",
        verbose_name="Şirket Logosu")

    def __str__(self):
        return self.clientTitle

    class Meta:
        verbose_name = 'Şirket'
        verbose_name_plural = 'Şirketler'

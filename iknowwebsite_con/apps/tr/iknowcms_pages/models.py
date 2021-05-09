from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class About(models.Model):
    aboutTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Hakkımızda",
        default="Hakkımızda",
        help_text="Maksimum 50 karakter, benzersiz.")

    aboutContent = RichTextField(
        verbose_name="Hakkımızda Yazısı")

    aboutImage = models.ImageField(
        upload_to="about/tr/",
        default="about/default_about_image.svg",
        verbose_name="Hakkımızda Görseli")

    def __str__(self):
        return self.aboutTitle

    class Meta:
        verbose_name = 'Hakkımızda'
        verbose_name_plural = 'Hakkımızda'


class Contact(models.Model):
    contactTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="İletişim",
        default="İletişim",
        help_text="Maksimum 50 karakter, benzersiz.")

    address = RichTextField(
        verbose_name="Adres")

    googleMap = models.TextField(
        verbose_name="Google Maps iFrame Link",
        help_text="Google Maps iFrame Linkini buraya yapıştırın.")

    phoneOne = models.CharField(
        max_length=20,
        verbose_name="Telefon Numarası",
        help_text="Bu alan zorunludur.")

    phoneTwo = models.CharField(
        max_length=20,
        verbose_name="Telefon Numarası",
        null=True,
        blank=True)

    phoneThree = models.CharField(
        max_length=20,
        verbose_name="Telefon Numarası",
        null=True,
        blank=True)

    emailOne = models.CharField(
        max_length=40,
        verbose_name="E-Posta",
        help_text="Bu alan zorunludur.")

    emailTwo = models.CharField(
        max_length=40,
        verbose_name="E-Posta",
        null=True,
        blank=True)

    emailThree = models.CharField(
        max_length=40,
        verbose_name="E-Posta",
        null=True,
        blank=True)

    facebook = models.CharField(
        max_length=100,
        verbose_name="Facebook Link",
        null=True,
        blank=True,
        help_text="Facebook sayfanızın linkini buraya yapıştırın.")

    twitter = models.CharField(
        max_length=100,
        verbose_name="Twitter Link",
        null=True,
        blank=True,
        help_text="Twitter sayfanızın linkini buraya yapıştırın.")

    instagram = models.CharField(
        max_length=100,
        verbose_name="Instagram Link",
        null=True,
        blank=True,
        help_text="Instagram sayfanızın linkini buraya yapıştırın.")

    youtube = models.CharField(
        max_length=100,
        verbose_name="Youtube Link",
        null=True,
        blank=True,
        help_text="Youtube sayfanızın linkini buraya yapıştırın.")

    linkedin = models.CharField(
        max_length=100,
        verbose_name="Linkedin Link",
        null=True,
        blank=True,
        help_text="Linkedin sayfanızın linkini buraya yapıştırın.")

    def __str__(self):
        return self.contactTitle

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = 'İletişim'


class Faq(models.Model):
    faqTitle = models.TextField(
        verbose_name="Soru")

    faqContent = models.TextField(
        verbose_name="Cevap")

    faqSlug = models.SlugField(
        verbose_name="Soru Uzantısı",
        help_text="Sorunun url uzantı formatı. Benzersiz.")

    def __str__(self):
        return self.faqTitle

    class Meta:
        verbose_name = "Sıkça Sorulan Soru"
        verbose_name_plural = 'Sıkça Sorulan Sorular'


class PrivacyPolicy(models.Model):
    policyTitle = models.CharField(
        max_length=50,
        verbose_name="Kanun",
        help_text="Maksimum 50 karakter, benzersiz.",
        default="Kişisel Verilerin Korunması Kanunu")

    policyContent = RichTextField(
        verbose_name="Kanun İçeriği")

    def __str__(self):
        return self.policyTitle

    class Meta:
        verbose_name = "Kanun"
        verbose_name_plural = 'Kanunlar'

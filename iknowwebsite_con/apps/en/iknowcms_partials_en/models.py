from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Carousel(models.Model):
    carouselTitle = models.CharField(
        unique=True,
        max_length=100,
        verbose_name="Image Title",
        help_text="Maximum 50 character. A section of the text in the image.")

    carouselImageLarge = models.ImageField(
        upload_to="carousel/en/large/",
        default="carousel/large/default_carouselLarge_image.png",
        verbose_name="Large Image",
        help_text="Size: 1200x400 px.")

    carouselImageMedium = models.ImageField(
        upload_to="carousel/en/medium/",
        default="carousel/medium/default_carouselMedium_image.png",
        verbose_name="Medium Image",
        help_text="Size: 720x400 px.")

    carouselImageSmall = models.ImageField(
        upload_to="carousel/en/small/",
        default="carousel/small/default_carouselSmall_image.png",
        verbose_name="Small Image", help_text="Size: 575x575 px.")

    carouselContent = RichTextUploadingField(
        verbose_name="Carousel Content")

    carouselBackgroundColor = models.CharField(
        max_length=20,
        verbose_name="Background Color",
        help_text="Sample: #ffbd59",
        default="#ffbd59")

    carouselSlug = models.SlugField(
        unique=True,
        max_length=100,
        verbose_name="Carousel Url Format",
        help_text="Url format of the Carousel Title, unique.")

    def __str__(self):
        return self.carouselTitle


class Testimonial(models.Model):
    testimonialTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Testimonial Title",
        help_text="Maximum 50 character, unique.")

    testimonialContent = models.TextField(
        verbose_name="Testimonial Content")

    testimonialImage = models.ImageField(
        upload_to="testimonial/en/",
        default="testimonial/default_testimonial_image.svg",
        verbose_name="Testimonial Image")

    def __str__(self):
        return self.testimonialTitle


class Client(models.Model):
    clientTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Client Title",
        help_text="Maximum 50 character, unique.")

    clientImage = models.ImageField(
        upload_to="client/en/",
        default="client/default_client_image.svg",
        verbose_name="Client Image")

    def __str__(self):
        return self.clientTitle

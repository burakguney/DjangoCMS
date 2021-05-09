from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Service(models.Model):
    serviceTitle = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Service Title",
        help_text="Maximum 50 character, unique.")

    serviceContent = RichTextField(
        verbose_name="Service Content")

    serviceIcon = models.CharField(
        max_length=50,
        default='<i class="fas fa-server fa-5x"></i>',
        verbose_name="Service Icon",
        help_text="You should paste Font Awesome Icon tag here. For icon size add fa-2x, fa-3x, fa-5x etc.. to end of the class.")

    serviceSlug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Service Slug",
        help_text="Url format of the Service Title, unique.")

    def __str__(self):
        return self.serviceTitle

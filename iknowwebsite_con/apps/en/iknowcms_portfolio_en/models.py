from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Portfolio(models.Model):
    portfolioTitle = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Project Title",
        help_text="Maximum 100 character, unique.")

    portfolioContent = RichTextUploadingField(
        verbose_name="Project Content")

    portfolioImage = models.ImageField(
        upload_to="project/en/%Y/%m/%d/",
        default="project/default_project_image.png",
        verbose_name="Project Image",
        help_text="Should be 600x400 pixels.")

    portfolioSlug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name="Project Slug",
        help_text="Url format of the Project Title, unique.")

    def __str__(self):
        return self.portfolioTitle

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

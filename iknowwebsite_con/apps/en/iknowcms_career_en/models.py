from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.


class Career(models.Model):
    careerTitle = models.CharField(
        max_length=50,
        verbose_name="Job Title")

    careerContent = RichTextField(
        verbose_name="Job Content")

    careerDate = models.DateTimeField(auto_now_add=True)

    careerLocation = models.CharField(
        max_length=50,
        verbose_name="Job Location",
        default="Turkey/Edirne")

    careerSlug = models.SlugField(
        verbose_name="Job Slug",
        help_text="Url format of the Job Title + Job Date, unique.")

    def __str__(self):
        return self.careerTitle

    class Meta:
        verbose_name = 'Job Advertisement'
        verbose_name_plural = 'Job Advertisements'

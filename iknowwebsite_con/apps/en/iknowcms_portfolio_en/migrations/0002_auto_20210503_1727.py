# Generated by Django 3.2 on 2021-05-03 14:27

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iknowcms_portfolio_en', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolioContent',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Project Content'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolioImage',
            field=models.ImageField(default='project/default_project_image.png', help_text='Should be 600x400 pixels.', upload_to='project/en/%Y/%m/%d/', verbose_name='Project Image'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolioSlug',
            field=models.SlugField(help_text='Url format of the Project Title, unique.', max_length=100, unique=True, verbose_name='Project Slug'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolioTitle',
            field=models.CharField(help_text='Maximum 100 character, unique.', max_length=100, unique=True, verbose_name='Project Title'),
        ),
    ]

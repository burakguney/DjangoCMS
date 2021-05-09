# Generated by Django 3.2 on 2021-04-30 13:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('careerTitle', models.CharField(max_length=50, verbose_name='Job Title')),
                ('careerContent', ckeditor.fields.RichTextField(verbose_name='Job Content')),
                ('careerDate', models.DateTimeField(auto_now_add=True)),
                ('careerLocation', models.CharField(default='Turkey/Edirne', max_length=50, verbose_name='Job Location')),
                ('careerSlug', models.SlugField(help_text='Url format of the Job Title + Job Date, unique.', verbose_name='Job Slug')),
            ],
            options={
                'verbose_name': 'Job Advertisement',
                'verbose_name_plural': 'Job Advertisements',
            },
        ),
    ]

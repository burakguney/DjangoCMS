# Generated by Django 3.2 on 2021-04-30 13:39

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolioTitle', models.CharField(help_text='Maksimum 100 karakter, benzersiz.', max_length=100, unique=True, verbose_name='Proje Başlığı')),
                ('portfolioContent', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Proje İçeriği')),
                ('portfolioImage', models.ImageField(default='portfolio/default_portfolio_image.png', help_text='600x600 piksel olmalı.', upload_to='portfolio/tr/%Y/%m/%d/', verbose_name='Proje Görseli')),
                ('portfolioSlug', models.SlugField(help_text='Proje başlığının url uzantı formatı, benzersiz.', max_length=100, unique=True, verbose_name='Proje Uzantısı')),
            ],
            options={
                'verbose_name': 'Proje',
                'verbose_name_plural': 'Projeler',
            },
        ),
    ]

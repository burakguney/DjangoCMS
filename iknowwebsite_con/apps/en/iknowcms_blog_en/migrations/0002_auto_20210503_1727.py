# Generated by Django 3.2 on 2021-05-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iknowcms_blog_en', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blogImage',
            field=models.ImageField(default='blog/default_blog_image.png', help_text='Should be 600x400 pixels.', upload_to='blog/en/%Y/%m/%d/', verbose_name='Blog Image'),
        ),
        migrations.AlterField(
            model_name='ipmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='ipmodel',
            name='ip',
            field=models.CharField(max_length=100, verbose_name='IP Address'),
        ),
    ]

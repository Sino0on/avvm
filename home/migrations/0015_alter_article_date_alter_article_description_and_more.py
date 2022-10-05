# Generated by Django 4.1.1 on 2022-10-05 10:03

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_partner_events_rer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/acrticle/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='events',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.eventcategory', verbose_name='Категорие'),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки'),
        ),
        migrations.AlterField(
            model_name='events',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='events',
            name='image',
            field=models.ImageField(upload_to='images/events/%Y/%m/%d', verbose_name='Изображание'),
        ),
        migrations.AlterField(
            model_name='events',
            name='preview',
            field=models.CharField(blank=True, default='Подробнее', max_length=155, null=True, verbose_name='Превью'),
        ),
        migrations.RemoveField(
            model_name='events',
            name='rer',
        ),
        migrations.AlterField(
            model_name='events',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='events',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Конетент'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='images/news/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='news',
            name='preview',
            field=models.CharField(blank=True, default='Подробнее...', max_length=100, null=True, verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=122, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='news',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='otherpage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='events',
            name='rer',
            field=models.ManyToManyField(blank=True, null=True, to='home.partner', verbose_name='Партнеры'),
        ),
    ]

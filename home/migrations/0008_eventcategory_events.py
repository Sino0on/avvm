# Generated by Django 4.1.1 on 2022-09-30 04:42

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_news_is_prior'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=123)),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.eventcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='images/events/%Y/%m/%d')),
                ('address', models.CharField(max_length=155)),
                ('translation', models.BooleanField(default='False', verbose_name='Трансляция')),
                ('start', models.DateTimeField(verbose_name='Начало')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(verbose_name='Окончание')),
                ('partner', models.CharField(max_length=123)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.eventcategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['-date'],
            },
        ),
    ]

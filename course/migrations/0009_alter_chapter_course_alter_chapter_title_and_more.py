# Generated by Django 4.1.1 on 2022-10-14 07:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0008_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='course_chapters', to='course.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='title',
            field=models.CharField(max_length=133, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course.coursecategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='images/courses/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(related_name='teachers', to=settings.AUTH_USER_MODEL, verbose_name='Учиеля'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_comment_course', to='course.coursecomment', verbose_name='Родитель'),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='text',
            field=models.CharField(max_length=255, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='task',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='chapter_tasks', to='course.chapter', verbose_name='Глава'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='task',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teacher', to=settings.AUTH_USER_MODEL, verbose_name='учитель'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=133, verbose_name='Название'),
        ),
    ]
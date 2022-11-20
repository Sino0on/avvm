from django.db import models
from home.models import *
from ckeditor.fields import RichTextField


class CourseCategory(models.Model):
    title = models.CharField(max_length=144, verbose_name='Название')
    date = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey('CourseCategory', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Подкатегория')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория курсов'
        verbose_name_plural = 'Категория курсов'


class Course(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название')
    description = RichTextField(verbose_name='Контент')
    preview = models.CharField(max_length=123, verbose_name='Контент')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/courses/', verbose_name='Изображение')
    teachers = models.ManyToManyField(User, related_name='teachers', verbose_name='Учиеля')
    category = models.ForeignKey(CourseCategory, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return f'Курс - {self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-date']


class Chapter(models.Model):
    title = models.CharField(max_length=133, verbose_name='Название')
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='course_chapters', verbose_name='Курс')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Глава'
        verbose_name_plural = 'Главы'


class Task(models.Model):
    title = models.CharField(max_length=133, verbose_name='Название')
    description = RichTextField(verbose_name='Текст')
    date = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT, related_name='teacher', verbose_name='учитель')
    chapter = models.ForeignKey(Chapter, on_delete=models.PROTECT, related_name='chapter_tasks', verbose_name='Глава')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class CourseComment(models.Model):
    text = models.CharField(max_length=255, verbose_name='Текст')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parent_comment_course', verbose_name='Родитель')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий - {self.text[0:10]}...'

    class Meta:
        verbose_name = 'Комментарий Курса'
        verbose_name_plural = 'Комментарии Курса'
        ordering = ['-date']


class TaskComment(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parent_comment_task')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий - {self.text[0:10]}...'

    class Meta:
        verbose_name = 'Комментарий Темы'
        verbose_name_plural = 'Комментарии Темы'
        ordering = ['-date']



from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.shortcuts import reverse


class User(AbstractUser):
    last_name = models.CharField(max_length=122, verbose_name='Фамилия')
    first_name = models.CharField(max_length=122, verbose_name='Имя')
    age = models.DateField(blank=True, null=True, verbose_name='Возраст')
    is_vrach = models.BooleanField(default=False, verbose_name='Врач')
    description = RichTextField(blank=True, default='Пусто', verbose_name='Описание')
    image = models.ImageField(upload_to='images/avatars/', blank=True, null=True, verbose_name='Аватар')
    profession = models.CharField(max_length=255, verbose_name='Профессия')

    def __str__(self):
        if self.first_name == '':
            return f'{self.username}'
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_joined']


class Mention(models.Model):
    description = RichTextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Упоминание'
        verbose_name_plural = 'Упоминания'
        ordering = ['-date']


class News(models.Model):
    title = models.CharField(max_length=122, verbose_name='Название')
    description = RichTextField(verbose_name='Конетент')
    preview = models.CharField(blank=True, null=True, default='Подробнее...', max_length=100, verbose_name='Превью')
    image = models.ImageField(upload_to='images/news/%Y/%m/%d/', verbose_name='Изображение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь', blank=True, null=True)
    is_prior = models.BooleanField(verbose_name='Важная новость', default=False)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('home:news_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']


class NewsImage(models.Model):
    image = models.ImageField(upload_to='images/news/%Y/%m/%d/')
    date = models.DateTimeField(auto_now_add=True)



class Article(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название')
    description = RichTextField(verbose_name='Контент')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    image = models.ImageField(upload_to='images/acrticle/%Y/%m/%d/', blank=True, null=True, verbose_name='Изображение')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return f'{self.title} | {self.user.first_name}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']


class ArticleFile(models.Model):
    file = models.FileField(upload_to='files/articles/%Y/%m/%d')
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class EventCategory(models.Model):
    title = models.CharField(max_length=123)
    subcategory = models.ForeignKey('EventCategory', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class Partner(models.Model):
    name = models.CharField(max_length=123, verbose_name='Название')
    description = models.CharField(max_length=255, blank=True, null=True,  verbose_name='Описание')
    image = models.ImageField(upload_to='images/partners/', blank=True, null=True, verbose_name='Картинка')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Events(models.Model):
    title = models.CharField(max_length=155, verbose_name='Название')
    description = RichTextField(verbose_name='Контент')
    preview = models.CharField(max_length=155, blank=True, null=True, default='Подробнее', verbose_name='Превью')
    image = models.ImageField(upload_to='images/events/%Y/%m/%d', verbose_name='Изображание')
    address = models.CharField(max_length=155)
    translation = models.BooleanField(default='False', verbose_name='Трансляция')
    start = models.DateTimeField(verbose_name='Начало')
    date = models.DateTimeField(auto_now_add='True', verbose_name='Дата загрузки')
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, verbose_name='Категорие')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    end = models.DateTimeField(verbose_name='Окончание')
    rer = models.ManyToManyField(Partner, blank=True, verbose_name='Партнеры')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('home:event_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ['-date']


class PageCatery(models.Model):
    title = models.CharField(max_length=123)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Страница на сайте'
        verbose_name_plural = 'Страницы на сайте'


class OtherPage(models.Model):
    title = models.CharField(max_length=144, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    on_page = models.ForeignKey(PageCatery, on_delete=models.CASCADE, related_name='pagecategory', verbose_name='Категория страницы')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Отдельная страница'
        verbose_name_plural = 'Отдельные страницы'

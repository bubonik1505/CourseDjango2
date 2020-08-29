from django.db import models
from django.contrib.auth.models import User
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

class Category(MPTTModel):
    '''Класс моделей. Создает соответствующую таблицу в базе данных'''
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100)
    description = models.TextField(
        verbose_name='Описание',
        max_length=1000,
        default='',
        blank=True
    )

    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    template = models.CharField(
        verbose_name='Шаблон',
        max_length=500,
        default='blog/post_list.html'
    )

    published = models.BooleanField(verbose_name='Отображать', default=True)
    paginated = models.PositiveIntegerField('Количество новостей на странице', default=5)
    sort = models.PositiveIntegerField('Порядок отображения', default=0)

    def __str__(self):
        return self.name

    #для корректного перевода на русский класса Category используем подкласс Meta
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    '''Класс тегов'''
    name = models.CharField(verbose_name='Имя', max_length=100, unique=True)
    slug = models.SlugField(verbose_name='url', max_length=100, unique=True)
    published = models.BooleanField(verbose_name='Отображать?', default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    '''Класс постов'''

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    title = models.CharField(verbose_name='Заголовок', max_length=100)
    subtitle = models.CharField('Подзаголовок', max_length=500, blank=True, null=True)
    mini_text = models.TextField(verbose_name='Краткое содержание', max_length=1000)
    text = models.TextField(verbose_name='Текст поста')
    created_date = models.DateTimeField(verbose_name='Дата создания', auto_now=True)
    slug = models.SlugField(verbose_name='url', max_length=100, unique=True)
    edit_date = models.DateTimeField(
        verbose_name='Дата редактирования',
        default=timezone.now,
        blank=True,
        null=True
    )

    published_date = models.DateTimeField(
        verbose_name='Дата публикации',
        default= timezone.now,
        blank=True,
        null=True
    )

    image = models.ImageField(
        verbose_name='Главная фотография',
        upload_to='post/',
        null=True,
        blank=True
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        blank=True
    )

    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True
    )

    template = models.CharField(
        verbose_name='Шаблон',
        max_length=500,
        default='blog/post_detail.html'
    )

    published = models.BooleanField(verbose_name='Опубликовать?', default=True)
    viewed = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)
    status = models.BooleanField(verbose_name='Для зарегистрированных', default=False)
    sort = models.PositiveIntegerField('Порядок сортировки', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('detail_post', kwargs={'category':self.category.slug, 'slug':self.slug})


class Comment(models.Model):
    '''Класс комментариев'''
    author = models.ForeignKey(
        User,
        verbose_name='Автор' ,
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        Post,
        verbose_name='Статья',
        on_delete=models.CASCADE
    )

    text = models.TextField(verbose_name='Комментарий')
    created_date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.text}{self.created_date}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
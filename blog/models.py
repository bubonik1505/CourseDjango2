from django.db import models

class Category(models.Model):
    '''Класс моделей. Создает соответствующую таблицу в базе данных'''
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100)

    def __str__(self):
        return self.name

    #для корректного перевода на русский класса Category используем подкласс Meta
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Tag(models.Model):
    '''Класс тегов'''
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(verbose_name='url', max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Post(models.Model):
    '''Класс постов'''
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    mini_text = models.TextField(verbose_name='Описание')
    text = models.TextField(verbose_name='Текст поста')
    created_date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    slug = models.SlugField(verbose_name='url', max_length=100, unique=True)

    def __str__(self):
        return f'{self.title}{self.mini_text}{self.text}{self.created_date}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    '''Класс комментариев'''
    text = models.TextField(verbose_name='Комментарий')
    created_date = models.DateTimeField(verbose_name='Дата публикации', auto_now=True)
    moderation = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.text}{self.created_date}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
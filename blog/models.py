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
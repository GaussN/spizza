import os

from django.contrib.auth.models import User
from django.db import models


class Pizza(models.Model):
    PIZZA_TYPES = (
        ('meat', 'мясная'),
        ('vegetarian', 'вегетарианская'),
    )
    DOUGH_TYPES = (
        ('thin', 'тонкое'),
        ('thick', 'толстое'),
    )
    SIZES = (
        (26, '26'),
        (30, '30'),
        (40, '40'),
    )

    id = models.AutoField(primary_key=True, db_index=True)
    image = models.ImageField(verbose_name='Фото')
    name = models.CharField(max_length=30, unique=True, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', max_length=150, default='')
    pizza_type = models.TextField(choices=PIZZA_TYPES, verbose_name='Тип')
    dough_type = models.TextField(choices=DOUGH_TYPES, verbose_name='Тип теста')
    size = models.IntegerField(choices=SIZES, verbose_name='Размер')

    def delete(self, using=None, keep_parents=False):
        try:
            os.remove(self.image.path)
        except Exception as e:
            print(e)
        return super().delete(using, keep_parents)

    def __str__(self):
        return f'{self.name} {self.price}'

"""
Класс модели нужен для работы с базой данных
"""
from django.contrib.auth.models import User
from django.db import models

from catalog.models import Pizza


class Cart(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, verbose_name='пицца')
    count = models.PositiveIntegerField(default=1, null=False, verbose_name='количество')

    def __str__(self):
        return f'{self.user.username} {self.pizza.name} {self.count}'

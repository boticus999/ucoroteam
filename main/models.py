from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    link = models.CharField('Укороченная ссылка', max_length=10, unique=True)
    url = models.CharField('Адрес в Интернете', max_length=150)

    def __str__(self):
        return f'{self.link}'

    class Meta:
        verbose_name = 'ссылка'
        verbose_name_plural = 'ссылки'

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

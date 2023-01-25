from django.contrib.auth.models import AbstractUser
from django.db import models

from store.models import Store


class User(AbstractUser):
    company = models.ForeignKey(Store, verbose_name='Компания', on_delete=models.SET_NULL, null=True,
                                related_name='users')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
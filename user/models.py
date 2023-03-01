from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import phone_validator


class User(AbstractUser):
    """Модель пользователя"""
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    middle_name = models.CharField("Отчество", max_length=200)
    phone = models.CharField("Телефон", validators=[phone_validator], max_length=13, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    def full_name(self):
        return f'{self.first_name} {self.username}'

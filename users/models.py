from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name=u'Usuário', max_length=20, unique=True)
    name = models.CharField(verbose_name=u'Nome', max_length=100, blank=True, null=True)
    email = models.EmailField(_('email address'), blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    class Meta:
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'
        ordering = ['-id']

    def __str__(self):
        return self.username
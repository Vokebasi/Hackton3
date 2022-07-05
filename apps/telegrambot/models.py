from django.db import models

class TeleSettings(models.Model):
    token = models.CharField(max_length=255, verbose_name='Токен')
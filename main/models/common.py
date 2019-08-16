from django.db import models
from django.contrib import admin


class Common(models.Model):
    created = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
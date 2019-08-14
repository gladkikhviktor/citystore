from django.db import models

class Common(models.Model):
    created = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

from django.conf import settings
from django.db import models


class Poll(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=50)


class Vote(models.Model):
    created = models.DateTimeField(auto_created=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
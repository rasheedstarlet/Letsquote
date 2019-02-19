from django.db import models

from django.conf import settings

from django.utils import timezone


class Quote(models.Model):
    body = models.TextField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body

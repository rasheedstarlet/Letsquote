from django.db import models

from django.contrib.auth.models import User

class Writer(User):
    name = models.CharField(max_length=25)

class Quote(models.Model):
    body = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.title

from django.db import models
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    photo = models.CharField(max_length=255)  # Строка с путем к изображению

    def __str__(self):
        return self.name


# Create your models here.

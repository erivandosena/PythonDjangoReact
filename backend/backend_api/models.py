from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=200)
    isnb = models.CharField(max_length=20)

    def __str__(self):
        return self.title
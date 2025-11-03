from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


class Topic(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
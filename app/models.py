from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=68, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    title = models.CharField(max_length=68, unique=True)
    description = models.CharField(max_length=1000)
    solution = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

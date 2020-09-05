from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=68, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Algorithm(models.Model):
    name = models.CharField(max_length=68, unique=True)
    description = models.CharField(max_length=1000)
    solution = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Algorithm, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

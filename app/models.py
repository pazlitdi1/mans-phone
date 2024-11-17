from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True)
    description = models.TextField()
    price = models.FloatField(default=0)

    def __str__(self):
        return self.title

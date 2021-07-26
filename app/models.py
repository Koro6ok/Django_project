from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=4000)
    slug = models.SlugField(null=True)
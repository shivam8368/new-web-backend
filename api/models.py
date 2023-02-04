from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Video(models.Model):
    id = models.CharField(primary_key=True, max_length=30)
    VideoLink = models.TextField(unique=True)
    description = models.TextField(default='Null')
    duration = models.CharField(max_length=200)
    thumb = models.TextField(unique=True)
    embed_code = models.TextField(unique=True)
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    quality = models.CharField(max_length=30)

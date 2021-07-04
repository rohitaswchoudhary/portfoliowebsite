from django.db import models
import uuid
from ckeditor.fields import RichTextField

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    body = RichTextField()

    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
         primary_key = True,
         unique = True,
         default = uuid.uuid4,
         editable = False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
         primary_key = True,
         unique=True,
         default = uuid.uuid4,
         editable = False)

    def __str__(self):
        return self.title
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
         primary_key = True,
         unique = True,
         default = uuid.uuid4,
         editable = False)

    def __str__(self):
        return self.name
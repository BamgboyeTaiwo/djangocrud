from time import timezone
from turtle import title
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Details(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.TextField(max_length=255)

class blogs():

    title = models.CharField(max_length=200)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    slug=models.SlugField(max_length=100, unique=True)
    # published = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog:single', args=[self.slug])

    def __str__(self):
        return self.title



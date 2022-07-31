from asyncio.windows_events import NULL
from tkinter import CASCADE
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import User
class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    post = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateField()


class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comment")
    comment = models.CharField(max_length=100)

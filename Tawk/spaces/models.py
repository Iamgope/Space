from email.policy import default
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from datetime import datetime
from django.template.defaultfilters import slugify 
# Create your models here.


class space(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    image = models.CharField(max_length=511,null=True)
    About = models.TextField(null=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class subscription(models.Model):
    name = models.CharField(max_length=256)
    space_id = models.ForeignKey(space, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=256)
    is_member = models.BooleanField(default=TRUE)

    class Meta:
        unique_together = ('space_id', 'user')

    def __str__(self):
        return self.name


class Posts(models.Model):
    Space = models.ForeignKey(space, on_delete=models.CASCADE)
    Title = models.CharField(max_length=300)
    Content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    published_on = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ("-published_on",)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    Space = models.ForeignKey(space, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    commented_on = models.DateTimeField(default=datetime.now())
    Post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-commented_on',)

    def __str__(self):
        return self.comment

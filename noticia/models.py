from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django_editorjs_fields import EditorJsJSONField, EditorJsTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    content = models.JSONField()
    # image = models.ImageField(upload_to='img/notas/', null=True, blank=True)
    # video = models.URLField(null=False, blank=True, default='https://www.youtube.com')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Image(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='imagenes')
    image = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor.username} - {self.image.name}"
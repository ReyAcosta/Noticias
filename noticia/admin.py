from django.contrib import admin
from .models import Category, Label, Note, Image
# Register your models here.
admin.site.register(Note)
admin.site.register(Category)
admin.site.register(Label)
admin.site.register(Image)


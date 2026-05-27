from django.contrib import admin
from .models import Tasks, Categories,Tag

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Categories)
admin.site.register(Tag)
from django.contrib import admin
from .models import Tasks, Categories

# Register your models here.
admin.site.register(Tasks)
admin.site.register(Categories)
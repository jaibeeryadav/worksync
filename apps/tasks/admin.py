from django.contrib import admin
from .models import Tasks, Categories,Tag, Comments, Attachments

# Register your models here.
admin.site.register(Tasks),
admin.site.register(Categories),
admin.site.register(Tag),
admin.site.register(Comments),
admin.site.register(Attachments),
from django.db import models
from django.conf import settings

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tasks(models.Model):
    PRIORITY_CHOICES = [
        ("low","Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    STATUS_CHOICES= [
        ('todo',"To Do"),
        ('in_progress','In Progress'),
        ('completed',"Completed"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL,null=True, blank=True, related_name='tasks')
    title = models.CharField(max_length=220)
    description = models.CharField(blank=True)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


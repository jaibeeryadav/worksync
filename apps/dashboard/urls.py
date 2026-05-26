from django.urls import path
from .views import Dashboard_View

urlpatterns = [
    path('dashboard/', Dashboard_View.as_view(), name='dashboard'),    
]

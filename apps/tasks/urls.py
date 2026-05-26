from django.urls import URLPattern, path
from .views import TaskCreationView, TaskListView, TaskDeleteView, TaskDetailView, TaskUpdateView, CategoriesListView, CategoriesCreateView

urlpatterns = [
    path('',TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreationView.as_view(), name='task_create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('categories/', CategoriesListView.as_view(), name='category_list'),
    path('categories/create/', CategoriesCreateView.as_view(), name='category_create'),
]


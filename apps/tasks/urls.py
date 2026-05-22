from django.urls import URLPattern, path
from .views import TaskCreationView, TaskListView, TaskDeleteView, TaskDetailView, TaskUpdateView

urlpatterns = [
    path('',TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreationView.as_view(), name='task_create'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
]

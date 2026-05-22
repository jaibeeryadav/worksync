from django.shortcuts import render
from .models import Tasks
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

# Create your views here.

class TaskListView(LoginRequiredMixin,ListView):
    model = Tasks
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(
            user = self.request.user
        )

class TaskCreationView(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class= TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/task_update.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Tasks.objects.filter(
            user = self.request.user
        )
    
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')

    def get_queryset(self):
        return Tasks.objects.filter(
            user = self.request.user
        )
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Tasks
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Tasks.objects.filter(
            user = self.request.user
        )
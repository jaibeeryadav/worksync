from django.shortcuts import render
from .models import Tasks
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.db.models import Q

# Create your views here.

class TaskListView(LoginRequiredMixin,ListView):
    model = Tasks
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 2

    def get_queryset(self):
        queryset = Tasks.objects.filter(
            user = self.request.user
        )
        # search feature
        search_query = self.request.GET.get('q')
        priority = self.request.GET.get('priority')
        status = self.request.GET.get('status')

        if search_query:
            queryset=queryset.filter(
                Q(title__icontains=search_query)|
                Q(description__icontains=search_query)
            )
        if priority:
            queryset = queryset.filter(priority=priority)
        if status:
            queryset = queryset.filter(status = status)
        
        return queryset


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



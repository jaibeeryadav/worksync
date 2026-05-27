from django.shortcuts import render, redirect
from .models import Tasks, Categories,Tag, Comments
from .forms import TaskForm, CategoriesForm, TagForm, CommentsForm
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
        ordering = self.request.GET.get('ordering')


        if search_query:
            queryset=queryset.filter(
                Q(title__icontains=search_query)|
                Q(description__icontains=search_query)
            )
        if priority:
            queryset = queryset.filter(priority=priority)
        if status:
            queryset = queryset.filter(status = status)
        allowed_ordering = [
            "created_at",
            "-created_at"
        ]
        if ordering in allowed_ordering:
            queryset = queryset.order_by(ordering)
        return queryset


class TaskCreationView(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class= TaskForm
    template_name = 'tasks/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        task  = form.save(commit=False)
        task.user = self.request.user
        
        new_category = form.cleaned_data.get(
            "new_category"
        )
        if new_category:
            category, created = (Categories.objects.get_or_create(name = new_category, user = self.request.user,))
            task.category  = category
        task.save()
        form.save_m2m()

        new_tags = form.cleaned_data.get('new_tags')
        if new_tags:
            tags, created = (Tag.objects.get_or_create(name = new_tags, user = self.request.user,))
            task.tags.add(tags)
        return redirect('task_list')
    
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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentsForm()
        return context
    def post(self,request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = self.object
            comment.user = request.user
            comment.save()
            return redirect('task_detail', pk = self.object.pk)
        context = self.get_context_data()

        context["comment_form"] = form

        return self.render_to_response(context)
        

class CategoriesListView(LoginRequiredMixin, ListView):
    model = Categories
    template_name = 'tasks/category_list.html'
    context_object_name = 'categories'
    def get_queryset(self):
        return Categories.objects.filter(
            user = self.request.user
        )

class CategoriesCreateView(LoginRequiredMixin, CreateView):
    model = Categories
    form_class = CategoriesForm
    template_name = 'tasks/category_create.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tasks/tag_list.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'tasks/tag_create.html'
    success_url = reverse_lazy('tag_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
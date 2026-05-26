from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import now
from django.views.generic import TemplateView
from apps.tasks.models import Tasks
# Create your views here.

class Dashboard_View(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        tasks = Tasks.objects.filter(user = self.request.user)

        context['total_tasks'] = tasks.count()
        context['completed_tasks'] = tasks.filter(status = 'completed').count()
        context['pending_tasks'] = tasks.exclude(status='completed').count()
        context['overdue_tasks'] = tasks.filter(due_date__lt = now().date(),
                                                status__in=['todo', 'in_progress'],).count()
        context['recent_tasks'] = tasks[:2]

        return context
    
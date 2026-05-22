from django import forms
from .models import Tasks

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}),
        required=False,
    )

    class Meta:
        model = Tasks
        fields = ['title','description','priority','status','due_date']
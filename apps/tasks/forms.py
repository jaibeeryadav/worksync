from django import forms
from .models import Tasks,Categories

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={"type":"date"}),
        required=False,
    )
    new_category = forms.CharField(required=False)

    class Meta:
        model = Tasks
        fields = ['title','description','priority','status','due_date', 'category']

        new_category = forms.CharField(required=False)
        def __init__(self, *args, **kwargs):
            user = kwargs.pop("user")

            super().__init__(*args, **kwargs)

            self.fields["category"].queryset = (
                Categories.objects.filter(user=user)
            )


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name']


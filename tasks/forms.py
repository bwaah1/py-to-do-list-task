from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        input_formats=['%d.%m.%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={'placeholder': 'DD.MM.YYYY HH:MM'}),
        error_messages={
            'invalid': 'Enter a valid date/time in the format DD.MM.YYYY HH:MM.',
        },
    )

    class Meta:
        model = Task
        fields = ['name', 'status', 'deadline', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

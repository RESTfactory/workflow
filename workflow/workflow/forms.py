from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        allowed_steps = ()
        try:
            allowed_steps = self.instance.workflow.allowed_steps.all().values_list('id', 'name')
        except Exception as e:
            pass
        self.fields['current_step'].choices = allowed_steps

    class Meta:
        model = Task
        fields = ('name', 'workflow', 'target_contact_info', 'info', 'current_step', 'comments')

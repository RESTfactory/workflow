from django.contrib import admin
from .models import (
    ContactInfo,
    Status,
    Action,
    Step,
    Workflow,
    Task,
)
from .forms import (
    TaskForm,
)

class TaskAdmin(admin.ModelAdmin):
    form = TaskForm

admin.site.register(ContactInfo)
admin.site.register(Status)
admin.site.register(Action)
admin.site.register(Step)
admin.site.register(Workflow)
admin.site.register(Task, TaskAdmin)

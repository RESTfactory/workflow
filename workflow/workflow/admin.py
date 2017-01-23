from django.contrib import admin
from .models import (
    ContactInfo,
    Status,
    Action,
    Step,
    Workflow,
    Task,
    TaskInstance,
    TaskHistory,
)
from .forms import (
    TaskForm,
)

class TaskAdmin(admin.ModelAdmin):
    form = TaskForm

class TaskInstanceAdmin(admin.ModelAdmin):
    readonly_fields = ('name','data')

class TaskHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'task', 'task_instances')

admin.site.register(ContactInfo)
admin.site.register(Status)
admin.site.register(Action)
admin.site.register(Step)
admin.site.register(Workflow)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskInstance, TaskInstanceAdmin)
admin.site.register(TaskHistory, TaskHistoryAdmin)

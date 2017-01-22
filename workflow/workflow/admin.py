from django.contrib import admin
from .models import (
    ContactInfo,
    Status,
    Action,
    Workflow,
    Task,
)

admin.site.register(ContactInfo)
admin.site.register(Status)
admin.site.register(Action)
admin.site.register(Workflow)
admin.site.register(Task)

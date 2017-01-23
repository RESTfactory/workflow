from django.contrib import admin
from .models import (
    Action,
    Comment,
)

admin.site.register(Action)
admin.site.register(Comment)

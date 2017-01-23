from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from comments.models import (
    Comment,
)

class ContactInfo(models.Model):
    name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_cellphone = models.CharField(max_length=15)
    contact_email = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Action(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Step(models.Model):
    name = models.CharField(max_length=100)
    status = models.ForeignKey(Status)

    def __str__(self):
        return self.name

# class History(models.Model):
#     actions = Action.
#     # name = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.id

class AbstractWorkflow(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Workflow(AbstractWorkflow):
    allowed_steps = models.ManyToManyField(Step, blank=True)

    def __str__(self):
        return self.name

class Task(AbstractWorkflow):
    workflow = models.ForeignKey(Workflow, related_name="workflow_task")
    # nombre del shopper y número de teléfono del shopper
    target_contact_info = models.ForeignKey(ContactInfo, blank=True, null=True)
    # el feedback a entregar
    info = models.TextField()
    # paso actual de ejecucion de tarea
    current_step = models.ForeignKey(Step, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def taskHistoryHandler(sender, instance, created, *args, **kwargs):
    print("taskHistoryHandler")

post_save.connect(taskHistoryHandler, sender=Task)

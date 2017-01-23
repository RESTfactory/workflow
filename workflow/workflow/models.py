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

    def as_json(self):
        return dict(
            name=self.name,
            contact_name = self.contact_name,
            contact_cellphone = self.contact_cellphone,
            contact_email = self.contact_email,
            )

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

class AbstractTask(AbstractWorkflow):
    # nombre del shopper y número de teléfono del shopper
    target_contact_info = models.ForeignKey(ContactInfo, blank=True, null=True)
    # el feedback a entregar
    info = models.TextField(blank=True, null=True)
    # paso actual de ejecucion de tarea
    current_step = models.ForeignKey(Step, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True)

    class Meta:
        abstract = True

class Task(AbstractTask):
    workflow = models.ForeignKey(Workflow, related_name="workflow_task")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_json(self):
        task_comments = []
        for comment in self.comments.all():
            task_comments.append(comment.as_json())

        return dict(
            name=self.name,
            target_contact_info = self.target_contact_info.as_json(),
            info = self.info,
            current_step = self.current_step.name,
            workflow = self.workflow.name,
            comments = task_comments,
            created_at = str(self.created_at),
            updated_at = str(self.updated_at)
            )

    def __str__(self):
        return self.name

class TaskInstance(models.Model):
    name = models.CharField(max_length=100)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{name} ({updated_at})'.replace('{name}',self.name).replace('{updated_at}', str(self.created_at))

class TaskHistory(models.Model):
    name = models.CharField(max_length=100)
    task = models.OneToOneField(Task, related_name='history')
    task_instances = models.ManyToManyField(TaskInstance, blank=True)

    def __str__(self):
        return self.name

def taskHistoryHandler(sender, instance, created, *args, **kwargs):
    history = None

    try:
        history = TaskHistory.objects.get(task=instance)
    except Exception as e:
        history_name = '{instance_name} history'.replace('{instance_name}', instance.name)
        history = TaskHistory.objects.create(name=history_name, task=instance)
    finally:
        try:
            task_instance = TaskInstance.objects.create(name=instance.name, data=str(instance.as_json()))
            if(task_instance):
                history.task_instances.add(task_instance)
        except Exception as e:
            pass

post_save.connect(taskHistoryHandler, sender=Task)

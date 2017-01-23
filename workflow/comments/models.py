from django.db import models

class Action(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(models.Model):
    action = models.ForeignKey(Action, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_json(self):
        action_name = None
        try:
            action_name = self.action.name
        except Exception as e:
            pass

        return dict(
            action = action_name,
            content = self.content,
            created_at = str(self.created_at),
            updated_at = str(self.updated_at)
            )

    def __str__(self):
        return (self.content[:32]+'...') if len(self.content) > 32 else self.content

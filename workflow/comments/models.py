from django.db import models

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def as_json(self):
        return dict(
            content = self.content,
            created_at = str(self.created_at),
            updated_at = str(self.updated_at)
            )

    def __str__(self):
        return (self.content[:32]+'...') if len(self.content) > 32 else self.content

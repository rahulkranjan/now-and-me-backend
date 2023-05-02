from django.db import models

from users.models import User

class Thought(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'thoughts'

    def __str__(self):
        return str(self.content)
    

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    thought = models.ForeignKey(Thought, on_delete=models.CASCADE)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'replies'

    def __str__(self):
        return str(self.content)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="User", help_text="User")
    title = models.CharField(max_length=200, verbose_name="Title", help_text="Title")
    description = models.TextField(blank=True, null=True, verbose_name="Description", help_text="Description")
    complete = models.BooleanField(default=False, verbose_name="Complete", help_text="Complete")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created at", help_text="Created at")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
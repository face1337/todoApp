from users.models import CustomUser as User
from django.db import models


class TodoList(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class TodoItem(models.Model):
    taskStatus = [
        ("NS", "Not started"),
        ("BL", "Blocked"),
        ("PR", "In Progress"),
        ("DN", "Done")
    ]
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, default=None,
                                 related_name="assignee")
    category = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_to = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=taskStatus, default=taskStatus[0])
    high_priority = models.BooleanField(default=False)

    def __str__(self):
        return self.name


from django.db import models

class ClientTask(models.Model):
    task = models.CharField(max_length=255)
    assigned_to = models.IntegerField(null=True)
    assigned_by = models.IntegerField()

    STATUS_CHOICES = [
        (1, 'To Do'),
        (2, 'In Progress'),
        (3, 'Done'),
    ]
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]

    task_status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task


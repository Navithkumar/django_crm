from django.db import models

class notification(models.Model):
    notification_type = models.CharField(max_length=100)
    task_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    notification_content = models.CharField(max_length=100)
    is_read = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.notification_type

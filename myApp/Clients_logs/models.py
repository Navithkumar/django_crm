from django.db import models
from django.conf import settings


class Client_logs(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_logs')
    admin_id = models.IntegerField(null=True)
    logs = models.CharField(max_length=100)
    handle_by = models.IntegerField(null=True)
    STATUS_CHOICES = [(1, 'Proposal Sent'), (2, 'Contacted'), (3, 'On Hold'),(4,'Negotiation'),(5,'Lost'),(6,'Rejected')]
    status = models.IntegerField(choices=STATUS_CHOICES, default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.handle_by

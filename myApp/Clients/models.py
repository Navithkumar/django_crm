from django.db import models
from django.conf import settings


class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clients')
    parent = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='child_clients')
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    contact_number = models.BigIntegerField()
    company_website = models.URLField(max_length=200)
    company_linkedin = models.URLField(max_length=200)
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    last_contacted = models.DateField()
    project_description = models.CharField(max_length=100)
    
    STATUS_CHOICES = [(1, 'Active'), (2, 'Inactive'), (3, 'On Hold')]
    PRIORITY_CHOICES = [(1, 'High'), (2, 'Medium'), (3, 'Low')]

    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    document_upload = models.FileField(upload_to='static/file_uploads')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_name

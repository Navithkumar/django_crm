from django.db import models

class Client(models.Model):
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    contact_number = models.BigIntegerField(max_length=100)
    company_website = models.CharField(max_length=100)
    company_linkedin= models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    email = models.EmailField()
    lastcontacted = models.DateField()
    project_description=models.CharField(max_length=100)
    status = models.IntegerField(default=1)
    priority = models.IntegerField(default=1)
    document_upload = models.FileField(upload_to='static/file_uploads')

    def __str__(self):
        return self.client_name

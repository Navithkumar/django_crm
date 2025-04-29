from rest_framework import serializers
from .models import Client

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'company_name',
            'company_address',
            'contact_number',
            'company_website',
            'company_linkedin',
            'client_name',
            'email',
            'lastcontacted',
            'project_description',
            'status',
            'priority',
            'document_upload',
        ]


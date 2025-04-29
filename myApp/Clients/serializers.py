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
            'last_contacted',
            'project_description',
            'status',
            'priority',
            'document_upload',
            'parent_id',
            'user_id',
        ]
        read_only_fields = ['created_at', 'updated_at'] 


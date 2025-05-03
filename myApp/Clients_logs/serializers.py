from rest_framework import serializers
from .models import Client_logs

class clientLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client_logs
        fields = [
            'admin_id',
            'logs',
            'handle_by',
            'status',
            'client_id'
        ]
        read_only_fields = ['created_at', 'updated_at'] 


from rest_framework import serializers
from .models import notification

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = notification
        fields = [
            'notification_type',
            'task_id',
            'user_id',
            'notification_content',
            'is_read'
        ]
        read_only_fields = ['created_at', 'updated_at'] 


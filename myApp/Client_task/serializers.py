from rest_framework import serializers
from .models import ClientTask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTask
        fields = [
            'task',
            'assigned_to',
            'assigned_by',
            'task_status',           
            'priority',
            'deadline'
        ]
        read_only_fields = ['created_at', 'updated_at'] 


from rest_framework import serializers
from .models import UserNotes

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotes
        fields = [
            'notes',
            'reminder_date',
            'client_id',
            'user_id',           
        ]
        read_only_fields = ['created_at', 'updated_at'] 


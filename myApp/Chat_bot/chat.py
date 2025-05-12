import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']

        allowed = await self.is_allowed_to_join(self.user, self.room_name)
        if allowed:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user.username,
                'message': message
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'user': event['user'],
            'message': event['message']
        }))

    @database_sync_to_async
    def is_allowed_to_join(self, user, room_name):
        from django.contrib.auth import get_user_model
        User = get_user_model()

        try:
            target_user = User.objects.get(username=room_name)
        except User.DoesNotExist:
            return False

        def get_role(u):
            if u.is_super_admin:
                return 'superadmin'
            elif u.is_admin:
                return 'admin'
            else:
                return 'salesperson'

        sender_role = get_role(user)
        receiver_role = get_role(target_user)

        allowed_pairs = {
            'superadmin': ['admin', 'salesperson'],
            'admin': ['superadmin', 'salesperson'],
            'salesperson': ['superadmin', 'admin'],
        }

        return receiver_role in allowed_pairs.get(sender_role, [])


import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import get_user
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import *




class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name=f'chat_{self.room_name}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
        )

      

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        roomname = text_data_json['roomname']

        await self.save_message(message, sender,receiver, roomname)

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
                'receiver': receiver,
                'roomname': roomname,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        receiver = event['receiver']
        roomname = event['roomname']

        
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'receiver': receiver,
            'roomname': roomname,
        }))

    @sync_to_async
    def save_message(self, message, sender,receiver, roomname):
        sender = User.objects.get(username=sender)
        receiver = User.objects.get(username=receiver)
        room = Chat.objects.get(roomname=roomname)
        newmessage=Message.objects.create(sender=sender,receiver=receiver,content=message)
        newmessage.save()
        room.message.add(newmessage)
        room.save()



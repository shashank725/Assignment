from channels.generic.websocket import AsyncWebsocketConsumer
import json
from app.functionality import analyze_message

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # print("Scope=", self.scope['url_route'])
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        await self.accept()
        # Send a message indicating that someone has logged in
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                'type': 'chat_message',
                'message': 'Someone has logged in!'
            }
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Added Feature:
        text = "John likes the blue house at the end of the street."
        if message == text:
            message = await analyze_message(message)
            message['main'] = text
            print("Found the message !")

        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                'type': 'chat_message',
                'message': message,
                # 'username': event['username']
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(
            {
                'message': message,
                # 'username': event['username']
            }
        ))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.room_name
        )
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatRoomConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("Scope=", self.scope)
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.channel_layer.group_send(
            self.room_group_name, {'type': 'tester_message', 'tester': 'Hello! Connected...'}
        )
        return await super().connect()
    
    async def tester_message(self, event):
        tester = event['tester']
        await self.send(
            text_data=json.dumps({'tester': tester})
        )

    # async def receive(self, text_data=None, bytes_data=None):
    #     return await super().receive(text_data, bytes_data)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.room_name
        )
        return await super().disconnect(code)
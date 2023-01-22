from channels.consumer import AsyncConsumer
import json


class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("Connected", event)
        await self.send(
            {
                'type': 'websocket.accept'
            }
        )

    async def websocket_receive(self, event):
        print("Receive", event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        if not msg: 
            return False 
        response = {
            'message': msg
        }
        await self.send({
            'type': "websocket.send", 
            'text': json.dumps(response)
        })

    async def websocket_disconnect(self, event):
        print("disconnected", event)
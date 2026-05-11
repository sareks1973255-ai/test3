from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 20834477
api_hash = '08fe734379555d72c42399e1ba89ca68'

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print(client.session.save())

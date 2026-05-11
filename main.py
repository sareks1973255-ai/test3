from telethon import TelegramClient, events
from telethon.sessions import StringSession
import os

API_ID = 20834477
API_HASH = "08fe734379555d72c42399e1ba89ca68"
SESSION = ""

SOURCE_CHAT = -1001111111111
TARGET_CHATS = [
    -1002222222222,
    -1003333333333
]

client = TelegramClient(
    StringSession(SESSION),
    API_ID,
    API_HASH
)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    for chat in TARGET_CHATS:
        try:
            await client.forward_messages(
                chat,
                event.message
            )
            print(f"Forwarded to {chat}")
        except Exception as e:
            print(e)

print("Bot ishga tushdi...")
client.start()
client.run_until_disconnected()

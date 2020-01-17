from instabot.config import API
from telethon import TelegramClient
from telethon.tl.types.input_peer_chat import InputPeerChat

# API config: https://my.telegram.org/apps
# Official examples:
# https://github.com/LonamiWebs/Telethon/blob/0e38ab4/telethon_examples/interactive_telegram_client.py
# Docs: https://telethon.readthedocs.io/en/latest/basic/quick-start.html
# https://habr.com/ru/post/425151/

chat_id = 844216

client = TelegramClient('session-telethon', **API)
client.connect()
chat = InputPeerChat(chat_id)

total_count, messages, senders = client.get_message_history(chat, limit=10)

for msg in reversed(messages):
    # Format the message content
    if getattr(msg, 'media', None):
        content = '<{}> {}'.format(  # The media may or may not have a caption
        msg.media.__class__.__name__,
        getattr(msg.media, 'caption', ''))
    elif hasattr(msg, 'message'):
        content = msg.message
    elif hasattr(msg, 'action'):
        content = str(msg.action)
    else:
        # Unknown message, simply print its class name
        content = msg.__class__.__name__

    text = '[{}:{}] (ID={}) {}: {} type: {}'.format(
            msg.date.hour, msg.date.minute, msg.id, "no name",
            content)
    print(text)

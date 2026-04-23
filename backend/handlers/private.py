from ..bot import bot


@bot.message_handler(func=lambda x: True, chat_types=['private'])
def all_messages(msg):
    """Ответ а неизвестные сообщения"""
    bot.send_message(msg.chat.id, "Bla bla bla 🤪")
from .bot import bot
from telebot import types


# start message
@bot.message_handler(commands=["start"], chat_types=["private"])
def start_answer(msg):
    """ First bot answer

    Args:
        msg (_type_): first message to bot - /start
    """
    
    reply_markup = types.ReplyKeyboardMarkup()
    reg_btn = types.InlineKeyboardButton(text="Регистрация")
    reply_markup.add(reg_btn)
    bot.send_message(msg.chat.id,
                     "Привет! Я бот-помошник.\nДля использования бота нужно зарегистрироваться 👇👇👇",
                     reply_markup=reply_markup)
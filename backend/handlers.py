from .bot import bot
from telebot import types
from .const import *
from .registration import *
import datetime


# start message
@bot.message_handler(commands=["start"])
def start_answer(msg):
    """ First bot answer

    Args:
        msg (_type_): first message to bot - /start
    """
    
    bot.send_message(
        msg.chat.id,
        f"""Привет! Я личный бот помошник @Devilord_666 👹
Вот мои команды:
{'\n\t'.join([f"{k} - {v}" for k, v in COMMANDS.items()])}"""
        )


@bot.message_handler(commands=['reg'])
def registrate(msg):
    bot.send_message(msg.chat.id, "Отлично для этого мне нужно чтобы немного рассказал о себе 🤪")
    bot.register_next_step_handler(msg, registrate_user)


@bot.message_handler(func=lambda x: True, chat_types=['private', 'group'])
def all_messages(msg):
    bot.send_message(msg.chat.id, "Bla bla bla 🤪")


@bot.channel_post_handler(func=lambda x: True)
def channel_posts_handler(post):
    answer = f"Новый пост в канале '{post.chat.title}' - {post.chat.id} в {datetime.datetime.today()}"
    bot.send_message("777862419", answer)
    print(answer)

@bot.edited_channel_post_handler(func=lambda post: True)
def channel_posts_edition(post):
    answer = f"В канале '{post.chat.title}' - {post.chat.id} изменен пост: {post.message_id} в {post.date}"
    bot.send_message("777862419", answer)
    print(answer)

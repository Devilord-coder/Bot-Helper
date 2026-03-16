from bot import bot
from telebot import types


# start message
@bot.message_handler(commands=["start"])
def start_answer(msg):
    """ First bot answer

    Args:
        msg (_type_): first message to bot - /start
    """
    
    bot.send_message(msg.chat.id,
                     "Привет! Я личный бот помошник @Devilord_666")


bot.channel_post_handler(func=lambda x: True)
def channel_posts_handler(post):
    answer = f"Новый пост в канале '{post.chat.title}' - {post.chat.id} в {post.date}"
    bot.send_message("777862419", answer)
    bot.send_message("3673589375", answer)
    print(answer)

bot.edited_channel_post_handler(func=lambda post: True)
def channel_posts_edition(post):
    answer = f"В канале '{post.chat.title}' - {post.chat.id} изменен пост: {post.message_id} в {post.date}"
    bot.send_message("777862419", answer)
    bot.send_message("3673589375", answer)
    print(answer)

import datetime
from ..bot import bot
import os


@bot.channel_post_handler(func=lambda x: True)
def channel_posts_handler(post):
    """Посты в каналах"""
    answer = f"Новый пост в канале '{post.chat.title}' - {post.chat.id} в {datetime.datetime.today()}"
    bot.send_message(os.getenv("ADMIN_ID"), answer)
    print(answer)

@bot.edited_channel_post_handler(func=lambda post: True)
def channel_posts_edition(post):
    """Изменение постов в каналах"""
    answer = f"В канале '{post.chat.title}' - {post.chat.id} изменен пост: {post.message_id} в {post.date}"
    bot.send_message(os.getenv("ADMIN_ID"), answer)
    print(answer)

import datetime
from ..bot import bot
import os


@bot.channel_post_handler(func=lambda x: True)
def channel_posts_handler(post):
    """Посты в каналах"""
    answer = f"New post in channel '{post.chat.title}' (@{post.chat.username}) at {datetime.datetime.today()}"
    bot.send_message(os.getenv("ADMIN_ID"), answer)
    print(answer)
from ..bot import bot
from ..const import COMMANDS
from ..registration import registrate_user


@bot.message_handler(commands=["start"])
def start_answer(msg):
    """ First bot answer"""

    bot.send_message(
        msg.chat.id,
        f"""Привет! Я личный бот помошник @Devilord_666 👹
Вот мои команды:
{'\n\t'.join([f"{k} - {v}" for k, v in COMMANDS.items()])}"""
        )


@bot.message_handler(commands=['reg'])
def registrate(msg):
    """Обработчик команды /reg"""
    bot.send_message(msg.chat.id, "Отлично для этого мне нужно чтобы немного рассказал о себе 🤪")
    bot.register_next_step_handler(msg, registrate_user)
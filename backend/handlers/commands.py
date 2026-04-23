from ..bot import bot
from ..const import COMMANDS
from ..registration import registrate_user
from backend.keyboards.inline_keyboards import social_networks_keyboard


@bot.message_handler(commands=["start"])
def start_answer(msg):
    """ First bot answer"""

    bot.send_message(
        msg.chat.id,
        f"""Привет! Я бот C3PO
Вот мои команды:
{'\n\t'.join([f"{k} - {v}" for k, v in COMMANDS.items()])}""",
        reply_markup=social_networks_keyboard()
        )


@bot.message_handler(commands=['reg'])
def registrate(msg):
    """Обработчик команды /reg"""
    bot.send_message(msg.chat.id, "Отлично для этого мне нужно чтобы немного рассказал о себе 🤪")
    bot.register_next_step_handler(msg, registrate_user)
from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def social_networks_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с нашими социльными сетями"""
    markup = InlineKeyboardMarkup()
    github_btn = InlineKeyboardButton(
        text="Наш GitHub",
        url="https://github.com/Devilord-coder"
    )
    dysnet_btn = InlineKeyboardButton(
        text="Наш сайт для развития навыков",
        url="http://danya.42post.ru:18080"
    )
    vk_btn = InlineKeyboardButton(
        text="Наш ВК",
        url="https://vk.com/devilord"
    )
    telegramm_btn = InlineKeyboardButton(
        text="Связь с админом👹",
        url="https://t.me/Devilord_666"
    )
    markup.add(
        github_btn,
        dysnet_btn,
        vk_btn,
        telegramm_btn
    )
    return markup
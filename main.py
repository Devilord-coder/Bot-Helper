import backend.handlers
from backend import bot, global_init
from backend.config import config

"""
██████╗ ███████╗ ██████╗ ██╗███████╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝
██████╔╝█████╗  ██║  ███╗██║███████╗
██╔══██╗██╔══╝  ██║   ██║██║╚════██║
██║  ██║███████╗╚██████╔╝██║███████║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝
            Inc, 2026

Telegram-Bot "C3PO - Helper"
Version: 2.0.0
Project GitHub: https://github.com/Devilord-coder/Bot-Helper.git
Our GitHub: https://github.com/Devilord-coder
For communication: https://t.me/Devilord_666
"""


def main():
    """ Main function that activates C3PO """
    
    print(f"Bot started working . . .")
    global_init(config.DATABASE_PATH)
    bot.infinity_polling(allowed_updates=['message', 'callback_query', 'edited_message', 'channel_post',
                                          'chat_member', 'my_chat_member'])


if __name__ == "__main__":
    main()

from .bot import bot
from .db_models import User
from .db_session import create_session


def registrate_user(msg):
    """Регистрация пользователя"""

    db = create_session()
    new_user = User(
        id=msg.from_user.id,
        name=msg.from_user.name,
        username=msg.from_user.username,
        about=msg.text
    )
    db.add(new_user)
    db.commit()
    db.close()
    bot.send_message(msg.chat.id, "Отлично! Вы успешно зарегистрированы 😎")
    print(f"New user registred - {new_user.name}({new_user.username}) at {new_user.created_date}")

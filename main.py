#  Copyright (c) ChernV (@otter18), 2021.

import os
import random

from setup import bot, logger
from webhook import app

# --------------- dialog params -------------------
dialog = {
    'hello': {
        'in': ['привет', 'hello', 'hi', 'privet', 'hey'],
        'out': ['Приветствую', 'Здравствуйте', 'Привет!']
    },
    'how r u': {
        'in': ['как дела', 'как ты', 'how are you', 'дела', 'how is it going'],
        'out': ['Хорошо', 'Отлично', 'Good. And how are u?']
    },
    'name': {
        'in': ['зовут', 'name', 'имя'],
        'out': [
            'Я telegram-template-bot',
            'Я бот шаблон, но ты можешь звать меня в свой проект',
            'Это секрет. Используй команду /help, чтобы узнать'
        ]
    }
}


# --------------- bot -------------------
@bot.message_handler(commands=['help', 'start'])
def say_welcome(message):
    logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used /start or /help')
    bot.send_message(
        message.chat.id,
        '<b>Привет, я упоротый бот</b>',
        parse_mode='html'
    )

#
# @bot.message_handler(func=lambda message: True)
# def echo(message):
#     for t, resp in dialog.items():
#         if sum([e in message.text.lower() for e in resp['in']]):
#             logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used {t}:\n\n%s', message.text)
#             bot.send_message(message.chat.id, random.choice(resp['out']))
#             return
#
#     logger.info(f'</code>@{message.from_user.username}<code> ({message.chat.id}) used echo:\n\n%s', message.text)
#     bot.send_message(message.chat.id, message.text)
#
# @bot.message_handler(commands=["id"])
# def get_id(message):
#     logger.info(f'</code>@{message.from_user.username}<code> used /id')
#     bot.send_message(message.chat.id, f"user_id = {message.chat.id}")

@bot.message_handler(commands=['test'])
def get_id(message):
    test = 5
    while test:
        bot.send_message(
            message.chat.id,
            '<b>Привет, я упоротый бот</b>',
            parse_mode='html'
        )
        test -= 1


if __name__ == '__main__':
    if os.environ.get("IS_PRODUCTION", "False") == "True":
        app.run()
    else:
        bot.infinity_polling()

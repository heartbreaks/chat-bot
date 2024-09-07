import logging

from core.tg_bot_handlers import GenericMessage


class TgBotHelper:
    def __init__(self, tg_bot_key, bot):
        self.bot = bot
        self.generic_message = GenericMessage(tg_bot_key, bot)


    def message_processing(self, message):
        self.generic_message.execute(message)

    def not_text_message(self, message):
        logging.info(f'Message from TG: {message}')
        self.bot.send_message(message, "Я умею работать только с текстовыми сообщениям", reply_to=message.id)

    def not_private_chat(self, message):
        logging.info(f'Message from TG: {message}')
        self.bot.send_message(message, "Я умею работать только в приватном чате", reply_to=message.id)
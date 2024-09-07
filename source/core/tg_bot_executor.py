import logging
import telebot

from core.tg_bot_helper import TgBotHelper


class TgBotExecutorHelper:
    def __init__(self):
        self.tg_bot_key = None
        self.bot = None
        self.bot_helper = None

    def create(self, tg_bot_key):
        self.bot = telebot.TeleBot(token=tg_bot_key, parse_mode='HTML', disable_web_page_preview=True)
        self.bot_helper = TgBotHelper(tg_bot_key, self.bot)
        return self

    def start(self) -> None:
        @self.bot.message_handler(content_types=['text'], chat_types=['private'])
        def message_processing(message):
            self.bot_helper.message_processing(message)

        @self.bot.message_handler(
            content_types=['audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                           'contact'], chat_types=['private'])
        def not_text_message(message):
            self.bot_helper.not_text_message(message)

        @self.bot.message_handler(func=lambda message: True)
        def not_private_chat(message):
            self.bot_helper.not_private_chat(message)

        try:
            self.bot.infinity_polling()
        except Exception as e:
            logging.error(f'Error on bot start polling: {self.tg_bot_config}. Error: {e}')


    def stop(self) -> None:
        self.bot.stop_bot()

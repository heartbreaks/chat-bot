import telebot
import json
import logging


class MessageExecutorHelper:
    def __init__(self):
        self.bot = None
        self.message = None

    def create(self, tg_bot_key, message):
        self.bot = telebot.TeleBot(tg_bot_key, parse_mode='HTML', disable_web_page_preview=True)
        self.message = message
        return self

    def start(self) -> None:
        data = None
        found_ingredients = []
        with open('data.json', 'r') as file:
            try:
                data = json.load(file)
                if data is not None:
                    ingredients = data.get('ingredients')
                    if ingredients is not None:
                        found_ingredients = self.find_ingredients(self.message.text, ingredients)
                        if len(found_ingredients) > 0:
                            self.prepare_and_send_answer(found_ingredients)
                        else:
                            self.send_message('Ингредиент не найден')
                    else:
                        raise Exception('Ingredients not found')
                else:
                    raise Exception('Json is empty')
            except Exception as e:
                logging.error(
                    f'Probably wrong json. Error: {e}')
                self.send_message('Во время чтения файла произошла ошибка. Проверьте json на валидность.')


    def send_message(self, text):
        try:
            self.bot.send_message(self.message.chat.id, text, reply_to_message_id=self.message.message_id)
        except Exception as e:
            logging.error(
                f'Can\'t send message text "{text}" in chat {self.message.chat.id}. Error: {e}')


    def find_ingredients(self, text, ingredients):
        found_ingredients = []
        for row in ingredients:
            logging.info(row)
            name = row.get('name').lower()
            if name.find(text.lower()) != -1:
                found_ingredients.append(row)
        return found_ingredients

    def prepare_and_send_answer(self, found_ingredients):
        message = ''
        for row in found_ingredients:
            if message != '':
                message += '----------------------------------\n'
            message += f'Название: {row.get('name')}\n'
            message += f'INCI: {row.get('INCI')}\n'
            message += f'Происхождение: {row.get('origin')}\n'
            message += f'Применение: {row.get('function')}\n'
            message += f'Опасность: {row.get('safety')}\n'
            message += f'Оценка: '
            for rate in range(row.get('rating')):
                message += '⭐'
            message += '\n'

        self.send_message(message)



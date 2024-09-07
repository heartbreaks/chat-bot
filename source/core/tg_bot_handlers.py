import logging

from threading import Thread
from core.message_executor import MessageExecutorHelper

class GenericMessage:

    def __init__(self, tg_bot_key, bot):
        self.bot = bot
        self.tg_bot_key = tg_bot_key
        self.message_threads = {}
        self.threads = {}
        self.started_pollers = []

    def execute(self, message):
        logging.info(f'Message from TG: {message}')
        self.send_typing_action(message)
        if self.is_command(message.text):
            self.delete_message(message)
            self.wrong_command_message(message)
            return
        self.add_message_thread(message)


    def send_typing_action(self, message):
        try:
            self.bot.send_chat_action(message.chat.id, 'typing')
        except Exception as e:
            logging.error(
                f'Can\'t send typing action in chat {message.chat.id}. Error: {e}')


    def wrong_command_message(self, message):
        self.send_message(message, "У меня нет доступных команд")


    def is_command(self, text):
        if text.find('/') == 0:
            return True
        return False


    def delete_message(self, message):
        try:
            self.bot.delete_message(message.chat.id, message.id)
        except Exception as e:
            logging.error(
                f'Can\'t delete message {message.id} in chat {message.chat.id}. Error: {e}')


    def send_message(self, message, text):
        try:
            self.bot.send_message(message.chat.id)
        except Exception as e:
            logging.error(
                f'Can\'t send message text "{text}" in chat {message.chat.id}. Error: {e}')


    def add_message_thread(self, message):
        thread_id = f'{message.chat.id}-{message.message_id}'
        self.remove_idle_threads()
        if thread_id not in self.started_pollers:
            executor_helper = MessageExecutorHelper()
            executor = executor_helper.create(tg_bot_key=self.tg_bot_key, message=message)
            thread = Thread(target=executor.start)
            thread.start()
            self.message_threads[thread_id] = thread
            self.started_pollers.append(thread_id)
            return executor
        else:
            logging.warning(f'Poller already started for chatgpt_thread: {chatgpt_thread["id"]}')
            return None


    def remove_idle_threads(self):
        for thread_id in list(self.message_threads.keys()):
            if not self.message_threads.get(thread_id).is_alive():
                if thread_id in self.started_pollers:
                    self.started_pollers.remove(thread_id)
                self.message_threads.pop(thread_id)
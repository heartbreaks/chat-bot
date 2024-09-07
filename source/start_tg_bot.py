import logging

from threading import Thread
from os import environ
from core.log import log_setup
from core.tg_bot_executor import TgBotExecutorHelper




if __name__ == '__main__':
    log_setup()
    tg_bot_key = environ.get('BOT_KEY')
    if tg_bot_key != '':
        executor_helper = TgBotExecutorHelper()
        executor = executor_helper.create(tg_bot_key=tg_bot_key)
        thread = Thread(target=executor.start)
        thread.start()
    else:
        logging.error('Tg bot key not found')
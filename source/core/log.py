import time
import logging

from os import environ


def log_setup() -> logging.Logger:
    logger = logging.getLogger(None)
    logger.setLevel(logging.getLevelName(environ.get('LOG_LEVEL')))
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(filename)s [LINE: %(lineno)d]: %(message)s')
    formatter.converter = time.gmtime

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.getLevelName(environ.get('LOG_LEVEL')))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger



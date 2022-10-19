import logging
import sys


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        frmt = logging.Formatter(fmt="[%(asctime)s: %(levelname)s] %(message)s", datefmt="%H:%M:%S")
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setFormatter(frmt)

        file_handler = logging.FileHandler("logs.log")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(frmt)

        logger.addHandler(handler)
        logger.addHandler(file_handler)
    return logger

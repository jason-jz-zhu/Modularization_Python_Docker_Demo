import logging

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'


def get_log(name: str) -> object:
    """Wrapper for standard logging."""
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter
    log_format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'
    formatter = logging.Formatter(log_format)
    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)
    logger.propagate = False

    return logger

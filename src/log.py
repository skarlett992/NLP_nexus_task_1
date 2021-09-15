import logging

logging.basicConfig()
logger = logging.getLogger('main')


def set_log_level(need_verbose):
    logger.setLevel(logging.DEBUG if need_verbose else logging.ERROR)

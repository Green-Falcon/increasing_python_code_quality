import logging
import logging.config

# config
logging.config.fileConfig("logging.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)
# config ends


def addition(a, b):
    if a % 2 == 0:
        logger.debug("We are in even numbers.")
        res = a + b
    else:
        logger.debug("We are in odd numbers.")
        res = a + b + 5

    return res


# res_1 = addition(5, 10)
# res_2 = addition(2, 20)
# logging.info(f"Result 1: {res_1} and Result 2: {res_2}")
# logger.info(f"Result 1: {res_1} and Result 2: {res_2}")

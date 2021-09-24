import logging
import logging.config
import first


# config
logging.config.fileConfig(disable_existing_loggers=False,
                          fname="logging.ini")
logger = logging.getLogger(__name__)
# end config


def find_result(num_1, num_2):
    logger.info("inside find_result function.")
    word_count = first.addition(num_1, num_2)
    logger.info("The final outcome is found.")

    return word_count


res = find_result(len("hello"), len("hi"))
logger.info(f"The outcome {res}")

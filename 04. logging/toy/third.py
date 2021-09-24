import logging


def func():
    logger = logging.getLogger(__name__)
    logger.info("Hi, foo")


class Car:
    logger = logging.getLogger(__name__)
    def model(self):
        self.logger.info("We are in model")


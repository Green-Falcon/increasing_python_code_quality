import logging
import logging.config
import third

logging.config.fileConfig(disable_existing_loggers=False,
                          fname="logging.ini")

logger = logging.getLogger(__name__)

logger.debug("program begins")
third.func()
my_car = third.Car()
my_car.model()
logger.debug("program ends")

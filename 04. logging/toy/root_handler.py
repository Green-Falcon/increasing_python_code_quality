import logging


# config starts
# logging.basicConfig(filename="my_root_log.log",
#                     level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)


# handler = logging.StreamHandler()
# handler.setLevel(logging.INFO)
# fmt_str = "[%(asctime)s]: %(levelno)-10s - %(name)s - %(message)s"
# frmatr = logging.Formatter(fmt=fmt_str)
# handler.setFormatter(frmatr)
# logging.getLogger().addHandler(handler)

logger = logging.getLogger(__name__)

#### end of config


logger.debug("program starts.")
a = 10 + 25
logger.info("program ends.")

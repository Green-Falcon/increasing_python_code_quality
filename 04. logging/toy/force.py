# import logging


# config starts
# handler = logging.StreamHandler()
# handler.setLevel(logging.DEBUG)
# fmt_str = "[%(asctime)s]: %(levelno)-10s - %(name)s - %(message)s"
# frmatr = logging.Formatter(fmt=fmt_str)
# handler.setFormatter(frmatr)
# logging.getLogger().addHandler(handler)
# logging.root.setLevel(logging.DEBUG)
#
# logging.basicConfig(filename="force.log", force=True)
#### end of config


# logging.debug("start")
# a = 10
# logging.debug("end")


# logger = logging.getLogger(__name__)
#
# logger.critical(f"**{logger.level}**")
# logger.critical(f"**{logger.root.level}**")


# logging_example.py
import logging

# Create a custom logger
logger = logging.getLogger(__name__)  # level is NOTSET

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('f_handler.log')
c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
logger.info("we are debugging.")
logger.warning(f"{logger.parent == logging.root}")

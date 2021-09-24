import logging

# logging.basicConfig(filename="file.log", level=logging.DEBUG)
# logger = logging.getLogger(__name__)


#### Beginning configuration
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.CRITICAL)

file_handler = logging.FileHandler("my_logs.log")
file_handler.setLevel(level=logging.INFO)

terminal_handler = logging.StreamHandler()
terminal_handler.setLevel(level=logging.DEBUG)

format_str = "[%(asctime)s]: %(name)s - %(levelname)s - %(lineno)d - %(message)s"
file_formatter = logging.Formatter(fmt=format_str)

file_handler.setFormatter(fmt=file_formatter)
terminal_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)
logger.addHandler(terminal_handler)
####  End of configuration


logger.debug("Program started.")
a = 20 + 5
logger.debug(f"The sum is {a}")


def function(a, b):
    if a == 0:
        logger.info("a is zero.")
        res = a + b
    else:
        logger.info("a is not zero.")
        res = a * b

    return res


def func_2(a, b):
    try:
        res = a / b
    except Exception:
        logger.exception("An exception has occurred.")
        res = 0

    return res


def make_list(inp):
    return [inp]


def new_append(inp_list, inp_val):
    my_logger = logging.getLogger(__name__)
    inp_list.append(inp_val)
    my_logger.critical("Check the name of the logger.")


# function(1, 2)
# function(0, 20)
# outcome = func_2(10, 0)
# logger.debug(f"********* {outcome}")
#
# my_string = "hi"
# list_1 = make_list(my_string)
# list_2 = make_list(my_string)
# new_append(list_1, "how")
# logger.critical(list_1)

# logger.critical(list_1 is list_2)
# logger.critical(list_1 == list_2)

logger.critical(logger.parent)
logger.critical(logger.parent == logging.getLogger())
logging.critical(logger.parent == logging.root)

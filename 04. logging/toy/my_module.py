import logging


root = logging.getLogger()
print(root.handlers)  # no handlers at this point
logging.warning('hello')  # calls basicConfig
print(root.handlers)  # has handler now

# create file handler
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add the handlers to the logger
root.addHandler(fh)

print(root.handlers)  # now has 2 handlers
root.warning('whats good')  # will only show to console
root.error('whats good')  # will show to console and file

random_logger = logging.getLogger('bogus')  # another logger, descendant from root
random_logger.warning('im random')  # will use root handlers, meaning it will show to console
random_logger.error('im random error')  # same as above, both console and file

# and you can ofc add handlers and what not differently to this non root logger

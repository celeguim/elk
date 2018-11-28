import logging
import time 


# create logger
filename = time.strftime("my-%Y-%m-%d-%M%S.log")
logger = logging.getLogger(filename)
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.FileHandler(filename)
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

# "application" code
logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

logging.shutdown()


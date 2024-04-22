import logging

logging.basicConfig(filename=".\\logs\\automation.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d%Y %I:%M:%S %P')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Debug")
logger.warning("Warming")
logger.info("Info")
logger.critical("Critical")
logger.error("Error")

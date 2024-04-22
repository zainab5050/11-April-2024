import logging


# # @staticmethod
# def loggen():
logging.basicConfig(filename="C://auto//april//logs//qq.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()

# logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.warning)

logger.debug("Debug")
logger.warning("Warming")
logger.info("Info")
logger.critical("Critical")
logger.error("Error")


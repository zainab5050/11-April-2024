import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d%Y %I:%M:%S %P')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

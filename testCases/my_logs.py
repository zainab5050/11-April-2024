import logging

logging.basicConfig(filename="C://auto//april//logs//logReport.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d %m %y     %I:%M:%S %p',
                    level=logging.DEBUG
                    )

logging.debug("Debugging")
logging.info("INFO")
logging.error("Error")
logging.critical("Critical")
logging.warning("Warning")

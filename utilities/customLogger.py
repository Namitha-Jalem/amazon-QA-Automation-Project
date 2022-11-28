import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="automation.log", filemode ='w', level=logging.ERROR,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print("loggen called")
        return logger

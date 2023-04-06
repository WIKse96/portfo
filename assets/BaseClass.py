import logging


class BaseClass:

    @staticmethod
    def test_logging():
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('E:/Wiktor/py/Projekty dostosowane/b2b/logging/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.CRITICAL)
        logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.WARNING)
        logger.setLevel(logging.NOTSET)

        return logger

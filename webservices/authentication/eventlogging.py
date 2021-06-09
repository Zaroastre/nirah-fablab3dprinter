import logging;

class Logger:
    def __init__(self, name: str):
        LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(
            filename="{}.log".format(name),
            level=logging.DEBUG,
            format=LOG_FORMAT
            );
        LOGGER: logging.Logger = logging.getLogger(__name__);

class LoggerFactory:
    @staticmethod
    def get_logger(class_name: str):
        return Logger(class_name=class_name);

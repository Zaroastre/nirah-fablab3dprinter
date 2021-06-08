from colorama import Fore, init;

init(autoreset=True);

class LogLevel:
    TRACE="TRACE"
    DEBUG="DEBUG"
    INFO="INFO"
    WARNING="WARNING"
    ERROR="ERROR"
    CRITICAL="CRITICAL"

class Logger:
    def __init__(self, class_name: type):
        self.__class_name: type = class_name;
    
    def __log(self, log_level: LogLevel, message: str):
        template: str = "";
        if (log_level == LogLevel.TRACE):
            template = "";
        elif (log_level == LogLevel.DEBUG):
            template = "";
        elif (log_level == LogLevel.INFO):
            template = "";
        elif (log_level == LogLevel.WARNING):
            template = "";
        elif (log_level == LogLevel.ERROR):
            template = "";
        elif (log_level == LogLevel.CRITICAL):
            template = "";
        print();

    def trace(self, message: str):
        self.__log()

class LoggerFactory:
    @staticmethod
    def get_logger(class_name: type):
        return Logger(class_name=class_name);
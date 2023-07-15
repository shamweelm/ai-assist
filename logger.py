import logging


def get_logger(logger_name, log_level=logging.INFO):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.propagate = False

    formatter = logging.Formatter(
        """TIME :- %(asctime)s, NAME :- %(name)s, LEVEL :- %(levelname)-8s,
        MESSAGE :- %(message)s, PROCESS INFO :- [%(process)d]%(processName)s, 
        THREAD INFO :- %(threadName)s[%(thread)d], PATHNAME :- %(pathname)s"""
        )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Added console logger if no handlers available
    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger
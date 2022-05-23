import logging.handlers
import logging
import os
import stat
from pythonjsonlogger import jsonlogger
from guternberg_api.configuration import LOGGING_LEVEL

try:
    logger = logging.getLogger(__name__)

    lobj_logger_dir_path = '.' + os.sep + 'log'
    mode = 0o777 | stat.S_IRUSR
    if not os.path.exists(lobj_logger_dir_path):
        os.makedirs(lobj_logger_dir_path, mode=0o777)
    filepath = lobj_logger_dir_path + os.sep + str(os.getcwd()).split(os.sep)[-1] + "_log"

    handler = logging.handlers.TimedRotatingFileHandler(filename=filepath, when='midnight', backupCount=20)

    try:
        if LOGGING_LEVEL.lower() == "critical":
            logger.setLevel(logging.CRITICAL)
            handler.setLevel(logging.CRITICAL)
        elif LOGGING_LEVEL.lower() == "error":
            logger.setLevel(logging.ERROR)
            handler.setLevel(logging.ERROR)
        elif LOGGING_LEVEL.lower() == "warning":
            logger.setLevel(logging.WARNING)
            handler.setLevel(logging.WARNING)
        elif LOGGING_LEVEL.lower() == "debug":
            logger.setLevel(logging.DEBUG)
            handler.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
            handler.setLevel(logging.INFO)
    except Exception as ex:
        logger.setLevel(logging.INFO)
        handler.setLevel(logging.INFO)

    formatter = jsonlogger.JsonFormatter('%(asctime)f %(levelname)s %(module)s %(funcName)s %(process)d %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

except Exception:
    raise

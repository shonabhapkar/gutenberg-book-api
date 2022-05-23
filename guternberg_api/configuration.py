import os
from configparser import ConfigParser

try:
    # creates i/p used for reading configurations from a file.
    lstr_config_file_path = os.path.dirname(
        os.path.realpath(__file__)) + os.path.sep + "data" + os.path.sep + "config.ini"

    # ===================================================================
    # read configurations
    # ===================================================================
    lobj_conf_parser = ConfigParser()
    lobj_conf_parser.read(lstr_config_file_path)

    # read Environment configurations
    DB_CONNECTION_URL = lobj_conf_parser.get("ENVIRONMENT", "DB_CONNECTION_URL")
    LOGGING_LEVEL = lobj_conf_parser.get("ENVIRONMENT", "LOGGING_LEVEL")
    BOOKS_BATCH_SIZE = lobj_conf_parser.getint("ENVIRONMENT", "BOOKS_BATCH_SIZE")

except Exception as ex:
    raise

import os
from configparser import ConfigParser

try:
    # =======================================================================
    # creates i/p used for reading configurations from a file.
    # =======================================================================
    lstr_config_file_path = os.path.dirname(
        os.path.realpath(__file__)) + os.path.sep + "data" + os.path.sep + "config.ini"
    ldict_sections__dict_of_properties = dict()
    ldict_sections__dict_of_properties["GENERAL"] = []
    ldict_sections__dict_of_properties["ENVIRONMENT"] = ["DB_CONNECTION_URL", "LOGGING_LEVEL"]

    # ===================================================================
    # read configurations
    # ===================================================================
    lobj_conf_parser = ConfigParser()
    lobj_conf_parser.read(lstr_config_file_path)

    # read Environment configurations
    DB_CONNECTION_URL = lobj_conf_parser.get("ENVIRONMENT", "DB_CONNECTION_URL")
    LOGGING_LEVEL = lobj_conf_parser.get("ENVIRONMENT", "LOGGING_LEVEL")

except Exception as ex:
    raise

import os

try:
    # =======================================================================
    # creates i/p used for reading configurations from a file.
    # =======================================================================
    lstr_config_file_path = os.path.dirname(
        os.path.realpath(__file__)) + os.path.sep + "data" + os.path.sep + "config.ini"
    ldict_sections__dict_of_properties = dict()
    ldict_sections__dict_of_properties["GENERAL"] = {}
    ldict_sections__dict_of_properties["ENVIRONMENT"] = {}

    # ===================================================================
    # read configurations
    # ===================================================================
    for lstr_section_name, ldict_properties in ldict_sections__dict_of_properties.items():
        pass


except Exception as ex:
    logger.error("\nError: " + str(ex), exc_info=True)

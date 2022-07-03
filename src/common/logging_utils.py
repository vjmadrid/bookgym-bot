# -*- coding: utf-8 -*-


import logging
import logging.config
import os
import yaml

from configs.default import (
    LOGGING_YAML_CONFIG_FILE_DEFAULT,
    LOGGING_PATH,
    LOGGING_APP_FILE_NAME,
    LOGGING_ERROR_FILE_NAME
)



def setup_logger(app_path=None, logging_config=None):

    logs_path = os.path.join(app_path, LOGGING_PATH)

    if not os.path.exists(logs_path):
        os.makedirs(logs_path)

    if logging_config is not None:

        #if log_file_path is not None:
        #    logging_config["handlers"]["info_file_handler"]["filename"] = log_file_path

        logging.config.dictConfig(logging_config)
    else:
        config_logging_path = app_path + "/" + LOGGING_YAML_CONFIG_FILE_DEFAULT

        with open(config_logging_path, "r") as fh:
            logging_config = yaml.safe_load(fh)

        if app_path is not None:
            logging_config["handlers"]["info_file_handler"]["filename"] = logs_path + "/" + LOGGING_APP_FILE_NAME
            logging_config["handlers"]["error_file_handler"]["filename"] = logs_path + "/" + LOGGING_ERROR_FILE_NAME

        logging.config.dictConfig(logging_config)


def create_logger(name):
    return logging.getLogger(name)

import logging
import logging.config
import os
import yaml

from configs.default import LOGGING_APP_FILE_NAME, LOGGING_ERROR_FILE_NAME

from .constants import (
    LOGGING_CONFIG_BASIC,
    LOGGING_CONFIG_YAML,
    DEFAULT_LOGGING_CONSOLE_FORMATTER_PATTERN,
)
from . import messages


def setup_console_logging(logging_level=logging.INFO):
    logging.basicConfig(level=logging_level, format=DEFAULT_LOGGING_CONSOLE_FORMATTER_PATTERN)


def setup_logging(config_file=None, logs_target_path=None, logging_level=logging.INFO):

    if config_file is None:
        print("No use configuration file. Using default configs")
        setup_console_logging(logging_level=logging_level)
        return LOGGING_CONFIG_BASIC

    print("\tUse config file : " + str(config_file))

    if logs_target_path is None or not logs_target_path:
        raise ValueError(messages.ERROR_LOGS_TARGET_PATH_INVALID_PARAMETER)

    print("\tUse logs target path : " + str(logs_target_path))

    if not os.path.exists(logs_target_path):
        os.makedirs(logs_target_path)

    # Check if exist config file
    if os.path.exists(config_file):

        config_file_extension = os.path.splitext(config_file)[1]
        is_yaml = config_file_extension in (".yaml", ".yml")

        if is_yaml:
            print("\tLoad YAML configuration : " + str(config_file))
            try:
                with open(config_file, "rt", encoding="utf-8") as file_handler:

                    logging_config = yaml.safe_load(file_handler)

                    logging_config["handlers"]["info_file_handler"]["filename"] = (
                        logs_target_path + "/" + LOGGING_APP_FILE_NAME
                    )
                    logging_config["handlers"]["error_file_handler"]["filename"] = (
                        logs_target_path + "/" + LOGGING_ERROR_FILE_NAME
                    )

                    logging.config.dictConfig(logging_config)

                    return LOGGING_CONFIG_YAML
            except Exception as exception:
                print(exception)
                print("\tFailed to load YAML configuration file. Using default configs")
        else:
            print("\tFailed to load configuration file. Using default configs")

    else:
        print("\tNo use configuration file. Using default configs")

    setup_console_logging(logging_level=logging_level)
    return LOGGING_CONFIG_BASIC

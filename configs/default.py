# -*- coding: utf-8 -*-


import os



# Define the application directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SOURCE_PATH = os.path.join(BASE_DIR, "src")
CONFIG_PATH = os.path.join(BASE_DIR, "configs")
DOCS_PATH = os.path.join(BASE_DIR, "docs")
TESTS_PATH = os.path.join(BASE_DIR, "tests")
DATA_PATH = os.path.join(BASE_DIR, "data")
REPORTS_PATH = os.path.join(BASE_DIR, "reports")


# *** Logging Config ***
LOGGING_SERVICE_NAME_KEY = "logging_service_name"
LOGGING_PATH_KEY = "./logs/"
LOGGING_FILE_NAME_KEY = "log_file.log"
LOGGING_MAIN_LEVEL_KEY = "logging_main_level"


ENABLE_CONSOLE_KEY = "enable_console"
ENABLE_NOTIFICATIONS_KEY = "enable_notifications"

LOGGING_PATH = "logs"
LOGGING_APP_FILE_NAME = "fitbot.log"
LOGGING_ERROR_FILE_NAME = "fitbot-error.log"

LOGGING_FORMATTER_PATTERN_GENERAL_DEFAULT= "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOGGING_FORMATTER_PATTERN_FILE_DEFAULT = f"[%(levelname)s]:%(asctime)s:%(module)s:%(lineno)d:%(name)s:%(message)s"
LOGGING_FORMATTER_PATTERN_CONSOLE_DEFAULT = "[%(levelname)s]: %(message)s"


LOGGING_YAML_CONFIG_FILE_DEFAULT = 'logging.yaml'

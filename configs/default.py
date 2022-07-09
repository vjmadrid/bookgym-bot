import os

import src.common.logging.constants as logging_constants


# Define the names ot the directories
SOURCE_DIRECTORY_NAME = "src"
CONFIG_DIRECTORY_NAME = "configs"
TEST_DIRECTORY_NAME = "tests"
DOC_DIRECTORY_NAME = "docs"
DATA_DIRECTORY_NAME = "data"
REPORT_DIRECTORY_NAME = "reports"
LOGS_DIRECTORY_NAME = "logs"
LOAD_DIRECTORY_NAME = "load"
TEMPLATE_DIRECTORY_NAME = "templates"
IMAGES_DIRECTORY_NAME = "images"
STATIC_DIRECTORY_NAME = "static"
DOWNLOAD_DIRECTORY_NAME = "downloads"


# Define the application directory path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Define the application directories path
SOURCE_DIR = os.path.join(BASE_DIR, SOURCE_DIRECTORY_NAME)
CONFIG_DIR = os.path.join(BASE_DIR, CONFIG_DIRECTORY_NAME)
TEST_DIR = os.path.join(BASE_DIR, TEST_DIRECTORY_NAME)
DOC_DIR = os.path.join(BASE_DIR, DOC_DIRECTORY_NAME)
DATA_DIR = os.path.join(BASE_DIR, DATA_DIRECTORY_NAME)
REPORT_DIR = os.path.join(BASE_DIR, REPORT_DIRECTORY_NAME)
LOGS_DIR = os.path.join(BASE_DIR, LOGS_DIRECTORY_NAME)
LOAD_DIR = os.path.join(BASE_DIR, LOAD_DIRECTORY_NAME)
TEMPLATE_DIR = os.path.join(BASE_DIR, TEMPLATE_DIRECTORY_NAME)
IMAGES_DIR = os.path.join(BASE_DIR, IMAGES_DIRECTORY_NAME)
STATIC_DIR = os.path.join(BASE_DIR, STATIC_DIRECTORY_NAME)
DOWNLOAD_DIR = os.path.join(BASE_DIR, DOWNLOAD_DIRECTORY_NAME)


# Define configuration files per environment
LOCAL_CONFIG_FILE = "configs.local"
DEVELOPMENT_CONFIG_FILE = "configs.local"
TESTING_CONFIG_FILE = "configs.testing"
STAGING_CONFIG_FILE = "configs.stage"
PRODUCTION_CONFIG_FILE = "configs.prod"

config_file_by_environment_name = dict(
    default=LOCAL_CONFIG_FILE,
    local=LOCAL_CONFIG_FILE,
    development=LOCAL_CONFIG_FILE,
    testing=TESTING_CONFIG_FILE,
    staging=STAGING_CONFIG_FILE,
    production=PRODUCTION_CONFIG_FILE,
)

# Define log configuration
# LOGGING_CONFIGURATION_FILE = CONFIG_DIR + "/" + logging_constants.DEFAULT_LOGGING_YAML_CONFIG_FILE

LOGGING_SERVICE_NAME_KEY = "logging_service_name"
LOGGING_PATH_KEY = "./logs/"
LOGGING_FILE_NAME_KEY = "log_file.log"
LOGGING_MAIN_LEVEL_KEY = "logging_main_level"


ENABLE_CONSOLE_KEY = "enable_console"
ENABLE_NOTIFICATIONS_KEY = "enable_notifications"

LOGGING_PATH = "logs"
LOGGING_APP_FILE_NAME = "bookgym.log"
LOGGING_ERROR_FILE_NAME = "bookgym-error.log"


LOGGING_YAML_CONFIG_FILE_DEFAULT = "logging.yaml"

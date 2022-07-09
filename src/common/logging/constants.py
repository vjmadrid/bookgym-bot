# Logging configuration type

LOGGING_CONFIG_BASIC = "LOGGING_CONFIG_BASIC"
LOGGING_CONFIG_YAML = "LOGGING_CONFIG_YAML"
LOGGING_CONFIG_CFG = "LOGGING_CONFIG_CFG"

# Logging configuration
LOGGING_SERVICE_NAME_KEY = "logging_service_name"
LOGGING_PATH_KEY = "logging_path"
LOGGING_FILE_NAME_KEY = "logging_file_name"
LOGGING_MAIN_LEVEL_KEY = "logging_main_level"


ENABLE_CONSOLE_KEY = "enable_console"
ENABLE_NOTIFICATIONS_KEY = "enable_notifications"


DEFAULT_LOGGING_FILE_FORMATTER_PATTERN = (
    "[%(levelname)s]:%(asctime)s:%(module)s:%(request_id)s:%(lineno)d:%(name)s:%(message)s"
)
DEFAULT_LOGGING_CONSOLE_FORMATTER_PATTERN = "[%(levelname)s]:[%(request_id)s] %(message)s"


DEFAULT_LOGGING_YAML_CONFIG_FILE = "logging.yaml"

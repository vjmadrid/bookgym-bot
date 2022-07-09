import unittest
import os
import tempfile
import pytest


from src.common.logging import utils
from src.common.logging.messages import ERROR_LOGS_TARGET_PATH_INVALID_PARAMETER
from src.common.logging.constants import LOGGING_CONFIG_BASIC, LOGGING_CONFIG_YAML

from configs.default import LOGGING_PATH


APP_DIR = os.path.dirname(os.path.abspath(__file__))

TEST_CFG_CONFIG_FILE = "test-logging.cfg"
TEST_YAML_CONFIG_FILE = "test-logging.yaml"
TEST_INVALID_PATH_YAML_CONFIG_FILE = TEST_YAML_CONFIG_FILE

TEST_PATH_CFG_CONFIG_FILE = os.path.join(APP_DIR, TEST_CFG_CONFIG_FILE)  #
TEST_PATH_YAML_CONFIG_FILE = os.path.join(APP_DIR, TEST_YAML_CONFIG_FILE)  #


TEST_LOGS_PATH = os.path.join(APP_DIR, LOGGING_PATH)


class TestLoggingUtil(unittest.TestCase):
    def test_logging_with_logs_target_path_none(self):
        with pytest.raises(ValueError) as excep:
            utils.setup_logging(config_file=TEST_PATH_YAML_CONFIG_FILE, logs_target_path=None)

        assert ERROR_LOGS_TARGET_PATH_INVALID_PARAMETER in str(excep.value)

    def test_logging_with_logs_target_path_empty(self):
        with pytest.raises(ValueError) as excep:
            utils.setup_logging(config_file=TEST_PATH_YAML_CONFIG_FILE, logs_target_path="")

        assert ERROR_LOGS_TARGET_PATH_INVALID_PARAMETER in str(excep.value)

    def test_logging_config_file_not_exist_and_logs_path_not_exist(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            logs_path = os.path.join(str(tmpdirname), LOGGING_PATH)
            result = utils.setup_logging(
                config_file=TEST_INVALID_PATH_YAML_CONFIG_FILE, logs_target_path=logs_path
            )

        assert result == LOGGING_CONFIG_BASIC

    def test_logging_config_file_not_exist_and_logs_path_exist(self):
        result = utils.setup_logging(
            config_file=TEST_INVALID_PATH_YAML_CONFIG_FILE, logs_target_path=TEST_LOGS_PATH
        )

        assert result == LOGGING_CONFIG_BASIC

    def test_logging_config_file_yaml(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            logs_path = os.path.join(str(tmpdirname), LOGGING_PATH)

            result = utils.setup_logging(
                config_file=TEST_PATH_YAML_CONFIG_FILE, logs_target_path=logs_path
            )

        assert result == LOGGING_CONFIG_YAML

    def test_logging_config_file_cfg(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            logs_path = os.path.join(str(tmpdirname), LOGGING_PATH)

            result = utils.setup_logging(
                config_file=TEST_PATH_CFG_CONFIG_FILE, logs_target_path=logs_path
            )

        assert result == LOGGING_CONFIG_BASIC

    def test_logging_default(self):
        result = utils.setup_logging()

        assert result == LOGGING_CONFIG_BASIC


if __name__ == "__main__":
    unittest.main()

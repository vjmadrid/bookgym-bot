import argparse
import json
import logging
import os
from datetime import datetime

from dotenv import load_dotenv

import src.common.logging.utils as logging_utils
from configs.default import LOGGING_CONFIGURATION_FILE, LOGS_DIR

# #####################
# General Configuration
# #####################

print(" [*] General Configuration")
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# app = Flask(__name__)
# app.register_blueprint(manager_bp)


# ##########################
# Load Environment Variables
# ##########################

print(" [*] Load Environment Variables")
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    load_dotenv()


# #####################
# Logging Configuration
# #####################

print(" [*] Logging Configuration")
logging_utils.setup_logging(
    config_file=LOGGING_CONFIGURATION_FILE,
    logs_target_path=LOGS_DIR,
    logging_level=logging.INFO,
)

LOG = logging.getLogger(__name__)


# #####################
# Check Argument
# #####################

"""
python app.py
    --email your.email@mail.com
    --password 1234
    --box-name avengergym
    --box-id 9876
    --booking-goal '{"0":{"time": "2245", "name": "Super Heroe"}}'
"""
print(" [*] Check Arguments")
parser = argparse.ArgumentParser()
parser.add_argument("--email", required=True, type=str)
parser.add_argument("--password", required=True, type=str)
parser.add_argument("--booking-goals", required=True, type=json.loads)
parser.add_argument("--box-name", required=True, type=str)
parser.add_argument("--box-id", required=True, type=int)
parser.add_argument("--days-in-advance", required=True, type=int, default=3)

args = parser.parse_args()
print("[*] args :: " + str(args))

input = {key: value for key, value in args.__dict__.items() if value != ""}
print("[*] Loaded Parameters :: " + str(input))

"""
    Start Flask Server
"""
# app.run(debug=True)


def job():
    LOG.info("Job 'Schedule' :: " + str(datetime.now()))
    # main(**input)


# schedule.every().hour.at("00:15").do(job)

# while True:
#    schedule.run_pending()
#    time.sleep(1)

job()

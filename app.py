import argparse
import json
import schedule
import time
import logging
import sys
import os

from datetime import datetime, timedelta


from src.client import AimHarderClient
from src.services import BookingService
from src.exceptions import BookingFailed
from src.logging_utils import setup_logger



APP_DIR = os.path.dirname(os.path.abspath(__file__))
setup_logger(app_path=APP_DIR)

LOG = logging.getLogger(__name__)


def get_class_to_book(day_classes: list[dict], target_time: str, class_name: str):
    day_classes = list(filter(lambda _class: target_time in _class["timeid"], day_classes))
    _class = list(filter(lambda _class: class_name in _class["className"], day_classes))

    if len(_class) == 0:
        return None

    return _class[0]["id"]


def main(email, password, booking_goals, box_name, box_id, days_in_advance):
    LOG.info("[INFO] Starting the booking process ...")

    aimharder_client = AimHarderClient(
        email=email, password=password, box_id=box_id, box_name=box_name
    )

    target_day = datetime.today() + timedelta(days=days_in_advance)
    target_day_weekday = str(target_day.weekday())
    target_day_value = target_day.strftime("%d-%m-%Y")
    LOG.info(f"[INFO] Set a target day : {target_day_value} ('{target_day_weekday}' in the week)")

    LOG.info("[INFO] Obtaining booking parameters from the user")
    booking_parameters_list = BookingService.get_booking_goal_time(booking_goals, target_day)

    # Check Boo
    if (booking_parameters_list is None) or (len(booking_parameters_list) == 0):
        LOG.info(f"[INFO] No booking parameters defined for the target day : {target_day_value}")
    else:

        num_booking_parameters_list = len(booking_parameters_list)
        count_reserved_class = 0
        LOG.info(
            f"[INFO] Detected {num_booking_parameters_list} class/es to book -> "
            + str(booking_parameters_list)
        )

        for i in range(num_booking_parameters_list):

            target_time = booking_parameters_list[i]["time"]
            target_name = booking_parameters_list[i]["name"]

            LOG.info(
                f"[INFO] Initialising the booking process for : '{target_time} - {target_name}'"
            )

            LOG.info("[INFO] Search for the class in the classes of the day ...")
            day_classes = aimharder_client.get_classes(target_day)
            class_id = get_class_to_book(day_classes, target_time, target_name)

            # Verify that the class exists and has ID
            if class_id is None:
                LOG.info(
                    f"[RESULT] There is no '{target_time} - {target_name}' class for that day "
                    + str(target_day.strftime("%d-%m-%Y"))
                )
            else:
                LOG.info(
                    f"[INFO] Identified class '{target_time} - {target_name}' with ID {class_id}"
                )
                try:
                    aimharder_client.book_class(target_day, class_id)
                    count_reserved_class = count_reserved_class + 1
                except BookingFailed as excep:
                    LOG.info(
                        f"[RESULT] [BookingFailed] '{target_time} - {target_name}' class booking failure due to reason : '"
                        + str(excep)
                    )
                except:
                    LOG.info("Something else went wrong")

        target_day_value = target_day.strftime("%d-%m-%Y %H:%M:%S")
        LOG.info(
            f"[RESULT] '{count_reserved_class}' Bookings made for the day : "
            + str(target_day_value)
        )


if __name__ == "__main__":
    """
    python src/main.py
        --email your.email@mail.com
        --password 1234
        --box-name avengergym
        --box-id 9876
        --booking-goal '{"0":{"time": "2245", "name": "Super Heroe"}}'
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--email", required=True, type=str)
    parser.add_argument("--password", required=True, type=str)
    parser.add_argument("--booking-goals", required=True, type=json.loads)
    parser.add_argument("--box-name", required=True, type=str)
    parser.add_argument("--box-id", required=True, type=int)
    parser.add_argument("--days-in-advance", required=True, type=int, default=3)
    args = parser.parse_args()

    input = {key: value for key, value in args.__dict__.items() if value != ""}
    # print("[*] Loaded Parameters :: " + str(input))


def job():
    LOG.info("[*] Job 'Schedule' :: " + str(datetime.now()))
    main(**input)

schedule.every().hour.at("00:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


import logging
from datetime import datetime, timedelta

from src.bookgym.messages import (
    ERROR_BOOKING_GOALS_JSON_INVALID_PARAMETER,
    ERROR_TARGET_DAY_INVALID_PARAMETER,
)
from src.client import AimHarderClient
from src.exceptions import BookingFailed
from src.services import BookingService

LOG = logging.getLogger(__name__)


class BookingService:
    @staticmethod
    def get_booking_goal_time(booking_goals_json, target_day: datetime):

        if (booking_goals_json is None) or (len(booking_goals_json) == 0):
            raise ValueError(ERROR_BOOKING_GOALS_JSON_INVALID_PARAMETER)

        if target_day is None:
            raise ValueError(ERROR_TARGET_DAY_INVALID_PARAMETER)

        weekday_str = str(target_day.weekday())

        # Check if weekday_str exists
        if weekday_str in booking_goals_json:
            num_classes = len(booking_goals_json[weekday_str])
            result_list = []

            for i in range(num_classes):
                result_list.append(booking_goals_json[weekday_str][i])

            return result_list

        return None


class ExecutionService:
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
        LOG.info(
            f"[INFO] Set a target day : {target_day_value} ('{target_day_weekday}' in the week)"
        )

        LOG.info("[INFO] Obtaining booking parameters from the user")
        booking_parameters_list = BookingService.get_booking_goal_time(booking_goals, target_day)

        # Check Boo
        if (booking_parameters_list is None) or (len(booking_parameters_list) == 0):
            LOG.info(
                f"[INFO] No booking parameters defined for the target day : {target_day_value}"
            )
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

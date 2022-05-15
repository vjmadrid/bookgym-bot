# -*- coding: utf-8 -*-


import logging

from datetime import datetime

from src.messages import (
    ERROR_BOOKING_GOALS_JSON_INVALID_PARAMETER,
    ERROR_TARGET_DAY_INVALID_PARAMETER,
)


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

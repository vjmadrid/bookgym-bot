# -*- coding: utf-8 -*-


import unittest
import pytest

from src.bookgym.services import BookingService
from src.bookgym.messages import (
    ERROR_BOOKING_GOALS_JSON_INVALID_PARAMETER,
    ERROR_TARGET_DAY_INVALID_PARAMETER,
)
from tests.unit.bookgym.bookgym_dummy_data_factory import BookgymDummyDataFactory


class TestBookingService(unittest.TestCase):

    # Check booking_goals_json errors
    def test_get_booking_goal_time_with_booking_goals_json_null(self):
        with pytest.raises(ValueError) as excep:
            BookingService.get_booking_goal_time(None, BookgymDummyDataFactory.TEST_TARGET_DAY)

        assert ERROR_BOOKING_GOALS_JSON_INVALID_PARAMETER in str(excep.value)

    def test_get_booking_goal_time_with_booking_goals_json_empty(self):
        with pytest.raises(ValueError) as excep:
            BookingService.get_booking_goal_time(BookgymDummyDataFactory.TEST_EMPTY_BOOKING_GOALS_JSON, BookgymDummyDataFactory.TEST_TARGET_DAY)

        assert ERROR_BOOKING_GOALS_JSON_INVALID_PARAMETER in str(excep.value)

    # Check target_day errors
    def test_get_booking_goal_time_with_target_day_null(self):
        with pytest.raises(ValueError) as excep:
            BookingService.get_booking_goal_time(BookgymDummyDataFactory.TEST_ONE_DAY_ONE_CLASS_BOOKING_GOALS_JSON, None)

        assert ERROR_TARGET_DAY_INVALID_PARAMETER in str(excep.value)

    # Check get_booking_goal_time
    def test_get_booking_goal_time_with_invalid_target_day(self):

        result_list = BookingService.get_booking_goal_time(
            BookgymDummyDataFactory.TEST_ONE_DAY_ONE_CLASS_BOOKING_GOALS_JSON, BookgymDummyDataFactory.TEST_INVALID_TARGET_DAY
        )

        assert result_list is None

    def test_get_booking_goal_time_with_invalid_day_booking_goals_json(self):

        result_list = BookingService.get_booking_goal_time(
            BookgymDummyDataFactory.TEST_INVALID_DAY_BOOKING_GOALS_JSON, BookgymDummyDataFactory.TEST_TARGET_DAY
        )

        assert result_list is None

    def test_get_booking_goal_time_with_one_day_one_class_booking_goals_json(self):

        result_list = BookingService.get_booking_goal_time(
            BookgymDummyDataFactory.TEST_ONE_DAY_ONE_CLASS_BOOKING_GOALS_JSON, BookgymDummyDataFactory.TEST_TARGET_DAY
        )

        assert result_list is not None
        assert len(result_list) == 1

        assert result_list[0]["time"] == "2230"
        assert result_list[0]["name"] == "test"

    def test_get_booking_goal_time_with_some_days_one_class_booking_goals_json(self):

        result_list = BookingService.get_booking_goal_time(
            BookgymDummyDataFactory.TEST_SOME_DAYS_ONE_CLASS_BOOKING_GOALS_JSON, BookgymDummyDataFactory.TEST_TARGET_DAY
        )

        assert result_list is not None
        assert len(result_list) == 1

        assert result_list[0]["time"] == "2230"
        assert result_list[0]["name"] == "test"

    def test_get_booking_goal_time_with_one_day_some_classes_booking_goals_json(self):

        result_list = BookingService.get_booking_goal_time(
            BookgymDummyDataFactory.TEST_ONE_DAY_SOME_CLASSES_BOOKING_GOALS_JSON, BookgymDummyDataFactory.TEST_TARGET_DAY
        )

        assert result_list is not None
        assert len(result_list) == 2

        assert result_list[0]["time"] == "2230"
        assert result_list[0]["name"] == "test"

        assert result_list[1]["time"] == "2330"
        assert result_list[1]["name"] == "test 2"

    def test_get_booking_goal_time_with_some_days_some_classes_booking_goals_json(self):

        result_list = BookingService.get_booking_goal_time(
            BookgymDummyDataFactory.TEST_SOME_DAYS_SOME_CLASSES_BOOKING_GOALS_JSON, BookgymDummyDataFactory.TEST_TARGET_DAY
        )

        assert result_list is not None
        assert len(result_list) == 2

        assert result_list[0]["time"] == "2230"
        assert result_list[0]["name"] == "test"

        assert result_list[1]["time"] == "2330"
        assert result_list[1]["name"] == "test 2"

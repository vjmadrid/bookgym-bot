# -*- coding: utf-8 -*-


import datetime


class BookgymDummyDataFactory:
    TEST_EMPTY_BOOKING_GOALS_JSON = {}
    TEST_INVALID_DAY_BOOKING_GOALS_JSON = {"3": [{"time": "2230", "name": "test"}]}
    TEST_ONE_DAY_ONE_CLASS_BOOKING_GOALS_JSON = {"0": [{"time": "2230", "name": "test"}]}
    TEST_ONE_DAY_SOME_CLASSES_BOOKING_GOALS_JSON = {
        "0": [
            {"time": "2230", "name": "test"},
            {"time": "2330", "name": "test 2"},
        ]
    }
    TEST_SOME_DAYS_ONE_CLASS_BOOKING_GOALS_JSON = {
        "0": [{"time": "2230", "name": "test"}],
        "1": [{"time": "2230", "name": "test 2"}],
    }
    TEST_SOME_DAYS_SOME_CLASSES_BOOKING_GOALS_JSON = {
        "0": [
            {"time": "2230", "name": "test"},
            {"time": "2330", "name": "test 2"},
        ],
        "1": [{"time": "2230", "name": "test 2"}],
    }

    TEST_TARGET_DAY = datetime.datetime(2022, 1, 3)  # 3 is Monday (0 weekday)
    TEST_INVALID_TARGET_DAY = datetime.datetime(2022, 1, 1)  # 1 is Saturday (4 weekday)

    TEST_BOX_NAME = "testgym"

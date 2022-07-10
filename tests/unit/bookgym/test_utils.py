# -*- coding: utf-8 -*-


import unittest

import pytest

from src.bookgym.messages import ERROR_BOX_NAME_INVALID_PARAMETER
from src.bookgym.utils import URLUtils
from tests.unit.bookgym.bookgym_dummy_data_factory import BookgymDummyDataFactory


class TestURLUtils(unittest.TestCase):
    def test_generate_book_endpoint_with_none(self):
        with pytest.raises(ValueError) as excep:
            URLUtils.generate_book_endpoint(None)

        assert ERROR_BOX_NAME_INVALID_PARAMETER in str(excep.value)

    def test_generate_book_endpoint_with_empty(self):
        with pytest.raises(ValueError) as excep:
            URLUtils.generate_book_endpoint("")

        assert ERROR_BOX_NAME_INVALID_PARAMETER in str(excep.value)

    def test_generate_book_endpoint(self):
        url = URLUtils.generate_book_endpoint(BookgymDummyDataFactory.TEST_BOX_NAME)

        assert url is not None
        assert (
            url
            == "https://" + str(BookgymDummyDataFactory.TEST_BOX_NAME) + ".aimharder.com/api/book"
        )

    def test_generate_classes_endpoint_with_none(self):
        with pytest.raises(ValueError) as excep:
            URLUtils.generate_classes_endpoint(None)

        assert ERROR_BOX_NAME_INVALID_PARAMETER in str(excep.value)

    def test_generate_classes_endpoint_with_empty(self):
        with pytest.raises(ValueError) as excep:
            URLUtils.generate_classes_endpoint("")

        assert ERROR_BOX_NAME_INVALID_PARAMETER in str(excep.value)

    def test_generate_classes_endpoint(self):
        url = URLUtils.generate_classes_endpoint(BookgymDummyDataFactory.TEST_BOX_NAME)

        assert url is not None
        assert (
            url
            == "https://"
            + str(BookgymDummyDataFactory.TEST_BOX_NAME)
            + ".aimharder.com/api/bookings"
        )

# -*- coding: utf-8 -*-


from datetime import datetime
from http import HTTPStatus
from bs4 import BeautifulSoup
from requests import Session

from src.bookgym.constants import (
    LOGIN_ENDPOINT,
    ERROR_TAG_ID,
)
from src.bookgym.exceptions import BookingFailed, IncorrectCredentials, TooManyWrongAttempts
from src.bookgym.messages import (
    MESSAGE_BOOKING_FAILED_UNKNOWN,
    MESSAGE_BOOKING_FAILED_NO_CREDIT,
    MESSAGE_BOOKING_FAILED_MORE_ONE_RESERVATION_SAME_TIME,
)
from src.bookgym.utils import URLUtils


class AimHarderClient:
    def __init__(self, email: str, password: str, box_id: int, box_name: str):
        self.session = self._login(email, password)
        self.box_id = box_id
        self.box_name = box_name

    @staticmethod
    def _login(email: str, password: str):
        session = Session()
        response = session.post(
            LOGIN_ENDPOINT,
            data={
                "login": "Log in",
                "mail": email,
                "pw": password,
            },
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser").find(id=ERROR_TAG_ID)
        if soup is not None:
            if TooManyWrongAttempts.key_phrase in soup.text:
                raise TooManyWrongAttempts
            elif IncorrectCredentials.key_phrase in soup.text:
                raise IncorrectCredentials
        return session

    def get_classes(self, target_day: datetime):
        response = self.session.get(
            URLUtils.generate_classes_endpoint(self.box_name),
            params={
                "box": self.box_id,
                "day": target_day.strftime("%Y%m%d"),
                "familyId": "",
            },
        )
        return response.json().get("bookings")

    def book_class(self, target_day: datetime, class_id: str):

        response = self.session.post(
            URLUtils.generate_book_endpoint(self.box_name),
            data={
                "id": class_id,
                "day": target_day.strftime("%Y%m%d"),
                "insist": 0,
                "familyId": "",
            },
        )

        if response.status_code == HTTPStatus.OK:
            response = response.json()

            # print("[*] response :: "+ str(response))

            if "bookState" in response and response["bookState"] == -2:
                raise BookingFailed(MESSAGE_BOOKING_FAILED_NO_CREDIT)

            if "bookState" in response and response["bookState"] == -12:
                raise BookingFailed(MESSAGE_BOOKING_FAILED_MORE_ONE_RESERVATION_SAME_TIME)

            if "errorMssg" not in response and "errorMssgLang" not in response:
                # booking went fine
                return

        raise BookingFailed(MESSAGE_BOOKING_FAILED_UNKNOWN)

# -*- coding: utf-8 -*-


from src.bookgym.messages import ERROR_BOX_NAME_INVALID_PARAMETER


class URLUtils:
    @staticmethod
    def generate_url_base(box_name):
        if (box_name is None) or (len(box_name) == 0):
            raise ValueError(ERROR_BOX_NAME_INVALID_PARAMETER)

        return f"https://{box_name}.aimharder.com"

    @staticmethod
    def generate_book_endpoint(box_name):
        return URLUtils.generate_url_base(box_name) + "/api/book"

    @staticmethod
    def generate_classes_endpoint(box_name):
        return URLUtils.generate_url_base(box_name) + "/api/bookings"

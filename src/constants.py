LOGIN_ENDPOINT = "https://aimharder.com/login"

ERROR_TAG_ID = "loginErrors"


def book_endpoint(box_name):
    return f"https://{box_name}.aimharder.com/api/book"


def classes_endpoint(box_name):
    return f"https://{box_name}.aimharder.com/api/bookings"


class ConsoleColourConstant:
    HEADER = "\033[95m"
    OK_BLUE = "\033[0;34m"
    OK_CYAN = "\033[96m"
    OK_GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    COLOR_OFF = "\033[0m"

    COLOR_BLACK = "\033[0;30m"
    COLOR_WHITE = "\033[0;37m"

    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

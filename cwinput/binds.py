from enum import Enum


class Keys(Enum):
    """
    List of non-printable characters.
    """
    NULL_CHARACTER = b"\0"
    START_OF_HEADING = b"\1"
    START_OF_TEXT = b"\2"
    END_OF_TEXT = b"\3"
    END_OF_TRANSMISSION = b"\4"
    ENQUIRY = b"\5"
    ACKNOWLEDGE = b"\6"

    AUDIBLE_BELL = b"\a"
    BACKSPACE = b"\b"
    HORIZONTAL_TAB = b"\t"
    LINE_FEED = b"\n"
    VERTICAL_TAB = b"\v"
    FORM_FEED = b"\f"
    CARRIAGE_RETURN = b"\r"
    ENTER = b"\r"

    SHIFT_OUT = b"\x0e"
    SHIFT_IN = b"\x0f"
    DATA_LINK_ESCAPE = b"\x10"
    DEVICE_CONTROL_1 = b"\x11"
    DEVICE_CONTROL_2 = b"\x12"
    DEVICE_CONTROL_3 = b"\x13"
    DEVICE_CONTROL_4 = b"\x14"
    NEGATIVE_ACKNOWLEDGE = b"\x15"
    SYNCHRONOUS_IDLE = b"\x16"
    END_OF_TRANSMISSION_BLOCK = b"\x17"
    CANCEL = b"\x18"
    END_OF_MEDIUM = b"\x19"
    SUBSTITUTE = b"\x1a"
    ESCAPE = b"\x1b"
    FILE_SEPARATOR = b"\x1c"
    GROUP_SEPARATOR = b"\x1d"
    RECORD_SEPARATOR = b"\x1e"
    UNIT_SEPARATOR = b"\x1f"

    ESCAPE_SEQ = b"\xe0"
    ESCAPE_SEQ_WIDE = b"\xc3\xa0"

    ARROW_UP = b"H"
    ARROW_LEFT = b"K"
    ARROW_DOWN = b"P"
    ARROW_RIGHT = b"M"

    HOME = b"G"
    PAGE_UP = b"I"
    END = b"O"
    PAGE_DOWN = b"Q"
    INSERT = b"R"
    DELETE = b"S"

    @classmethod
    def get(cls, value: str, escape: bool = False):
        """
        Get enum key by value, lists escape characters if `escape` flag is provided
        """
        escapes = [cls.ARROW_UP, cls.ARROW_LEFT, cls.ARROW_DOWN, cls.ARROW_RIGHT,
                   cls.HOME, cls.PAGE_UP, cls.END, cls.PAGE_DOWN, cls.INSERT, cls.DELETE]
        for item in Keys:
            if item.value == value:
                if item.value in escapes and not escape:
                    return None
                return item

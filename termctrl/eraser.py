from enum import Enum
from .common import escape


class Erase(Enum):
    LN_FROM_CURSOR = "[K"
    LN_TO_CURSOR = "[1K"
    LN = "[2K"
    SCR_BOT_FROM_LN = "[J"
    SCR_TOP_TO_LN = "[1J"
    SCR = "[2J"


def esc_erase(e: Erase) -> str:
    return escape(e.value)

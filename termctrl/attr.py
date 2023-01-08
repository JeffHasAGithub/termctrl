from enum import Enum
from .common import ANSI_ESC


class FgColor(Enum):
    """ANSI foreground color control values"""
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37


class BgColor(Enum):
    """ANSI background color control values"""
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47


def write_fg(clr: FgColor, text: str) -> str:
    clr = clr.value
    return f"{ANSI_ESC}[{clr}m{text}{ANSI_ESC}[0m"


def write_bg(clr: BgColor, text: str) -> str:
    clr = clr.value
    return f"{ANSI_ESC}[{clr}m{text}{ANSI_ESC}[0m"

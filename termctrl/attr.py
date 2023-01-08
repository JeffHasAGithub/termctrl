from enum import Enum


class Attr(Enum):
    """Base attribute class"""


class Format(Attr):
    """ANSI Formatting attributes"""
    RESET = 0
    BRIGHT = 1
    DIM = 2
    UNDERSCORE = 4
    BLINK = 5
    REVERSE = 7
    HIDDEN = 8


class Color(Attr):
    """Base color class"""


class FgColor(Color):
    """ANSI foreground colors"""
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37


class BgColor(Color):
    """ANSI background colors"""
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47

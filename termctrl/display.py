import sys
from .common import ANSI_ESC


def clear_ln_from_cursor(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[K")


def clear_ln_to_cursor(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[1K")

import sys
from .common import ANSI_ESC


def clear_ln_from_cursor(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[K")


def clear_ln_to_cursor(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[1K")


def clear_ln(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[2K")


def clear_up(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[1J")


def clear_dn(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[J")


def clear_screen(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[2J")

import sys
from .common import ANSI_ESC


def clear_ln_from_cursor(buffer=sys.stdout):
    """Clear line from the cursor to the end of the line"""
    buffer.write(f"{ANSI_ESC}[K")


def clear_ln_to_cursor(buffer=sys.stdout):
    """Clear line from beginning of the line up to the cursor"""
    buffer.write(f"{ANSI_ESC}[1K")


def clear_ln(buffer=sys.stdout):
    """Clear the current line"""
    buffer.write(f"{ANSI_ESC}[2K")


def clear_up(buffer=sys.stdout):
    """Clear screen from the current line up to the top of the screen"""
    buffer.write(f"{ANSI_ESC}[1J")


def clear_dn(buffer=sys.stdout):
    """Clear screen from the current line down to the bottom of the screen"""
    buffer.write(f"{ANSI_ESC}[J")


def clear_screen(buffer=sys.stdout):
    """Clear the entire screen"""
    buffer.write(f"{ANSI_ESC}[2J")

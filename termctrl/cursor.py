import sys
from .common import ANSI_ESC


def home(buffer=sys.stdout):
    """Reset cursor position to top-left corner of terminal"""
    buffer.write(f"{ANSI_ESC}[H")


def move(row: int, col: int, buffer=sys.stdout):
    """Move cursor to given row and col within terminal"""
    buffer.write(f"{ANSI_ESC}[{row};{col}H")


def move_up(count=1, buffer=sys.stdout):
    """Move cursor up {count} number of rows within terminal"""
    buffer.write(f"{ANSI_ESC}[{count}A")


def move_dn(count=1, buffer=sys.stdout):
    """Move cursor down {count} number of rows within terminal"""
    buffer.write(f"{ANSI_ESC}[{count}B")


def move_fw(count=1, buffer=sys.stdout):
    """Move cursor forward {count} number of cols within terminal"""
    buffer.write(f"{ANSI_ESC}[{count}C")


def move_bw(count=1, buffer=sys.stdout):
    """Move cursor backward {count} number of cols within terminal"""
    buffer.write(f"{ANSI_ESC}[{count}D")


def save(buffer=sys.stdout):
    """Save current cursor position"""
    buffer.write(f"{ANSI_ESC}[s")


def restore(buffer=sys.stdout):
    """Restore cursor to last saved position"""
    buffer.write(f"{ANSI_ESC}[u")

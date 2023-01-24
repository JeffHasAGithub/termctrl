from typing import NamedTuple
from .common import escape


class Position(NamedTuple):
    row: int
    col: int


def esc_move(row: int, col: int) -> str:
    """Move cursor to given row and col within terminal"""
    return escape(f"[{row};{col}H")


def esc_save() -> str:
    """Save current cursor position"""
    return escape("[s")


def esc_restore():
    """Restore cursor to last saved position"""
    return escape("[u")


def esc_query_position() -> str:
    return escape("[6n")

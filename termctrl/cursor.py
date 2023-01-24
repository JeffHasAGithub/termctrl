from typing import NamedTuple
from .common import escape
from .error import CursorError


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


def parse_position(pos: str) -> Position:
    pre, pos, suf = pos[:3], pos[3:-1], pos[-1]

    if pre != "^[[" or suf != "R":
        raise CursorError(f"Cursor error: {pos} is an invalid cursor query")

    row, col = pos.split(";")
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        raise CursorError(f"Cursor error: {row}, {col} cannot be converted"
                          " to an integer")

    return Position(row, col)

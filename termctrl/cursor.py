import sys
from .common import ANSI_ESC


def home(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[H")


def move(row: int, col: int, buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[{row};{col}H")


def move_up(count=1, buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}{count}A")


def move_dn(count=1, buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}{count}B")


def move_fw(count=1, buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}{count}C")


def move_bw(count=1, buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}{count}D")


def save(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[s")


def restore(buffer=sys.stdout):
    buffer.write(f"{ANSI_ESC}[u")

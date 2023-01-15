import sys
from .attr import Attr, esc_attrs
from .common import escape
from .cursor import esc_move, esc_save, esc_restore
from .eraser import Erase, esc_erase


class TermCtrl():
    def __init__(self, buffer=sys.stdout):
        self.buffer = buffer

    def write(self, s: str, *attrs: Attr):
        self.buffer.write(esc_attrs(s, *attrs))

    def writeln(self, s: str, *attrs: Attr):
        self.write(esc_attrs(s + "\n", *attrs))

    def erase(self, e: Erase):
        self.write(esc_erase(e))

    def home(self):
        self.write(esc_move(0, 0))

    def move(self, row: int, col: int):
        self.write(esc_move(row, col))

    def save(self):
        self.write(esc_save())

    def restore(self):
        self.write(esc_restore())

    def reset(self):
        self.write(escape("c"))

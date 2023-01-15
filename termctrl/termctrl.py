import sys
from .common import escape
from .attr import Attr, Format
from .cursor import esc_move, esc_save, esc_restore
from .eraser import Erase, esc_erase


class TermCtrl():
    def __init__(self, buffer=sys.stdout):
        self.buffer = buffer

    def write(self, s: str):
        self.buffer.write(s)

    def writeln(self, s: str):
        self.write(s + "\n")

    def erase(self, e: Erase):
        self.write(esc_erase(e))

    def home(self):
        self.write(esc_move(0, 0))

    def move(self, row: int, col: int):
        self.write(esc_move(row, col))

    def set_attr(self, attr: Attr):
        attr = attr.value
        self.write(escape(f"[{attr}m"))

    def reset_attrs(self):
        self.set_attr(Format.RESET)

    def reset_all(self):
        self.write(escape("c"))

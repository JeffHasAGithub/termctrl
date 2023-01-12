import sys
from .common import escape
from .eraser import Erase, esc_erase
from .attr import Attr, Format


class TermCtrl():
    def __init__(self, buffer=sys.stdout):
        self.buffer = buffer

    def write(self, s: str):
        self.buffer.write(s)

    def writeln(self, s: str):
        self.write(s + "\n")

    def erase(self, e: Erase):
        self.write(esc_erase(e))

    def set_attr(self, attr: Attr):
        attr = attr.value
        self.write(escape(f"[{attr}m"))

    def reset_attrs(self):
        self.set_attr(Format.RESET)

    def reset_all(self):
        self.write(escape("c"))

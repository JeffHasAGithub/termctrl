import sys
from .common import ANSI_ESC
from .attr import Attr, Format


class TermCtrl():

    def __init__(self, buffer=sys.stdout):
        self.buffer = buffer

    def write(self, s: str):
        self.buffer.write(s)

    def writeln(self, s: str):
        self.write(s + "\n")

    def set_attr(self, attr: Attr):
        attr = attr.value
        self.write(f"{ANSI_ESC}[{attr}m")

    def reset_attrs(self):
        self.set_attr(Format.RESET)

    def reset_all(self):
        self.write(f"{ANSI_ESC}c")

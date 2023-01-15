import unittest
from termctrl.attr import (Attr, FgColor,
                           BgColor, Format, esc_attrs)
from typing import NamedTuple


class TCase(NamedTuple):
    text: str
    attrs: tuple[Attr]
    want: str


class TestAttr(unittest.TestCase):
    def test_esc_attr(self):
        cases = (TCase("", (), ""),
                 TCase("Hello!", (FgColor.RED,),
                       "\033[0;31mHello!\033[0m"),
                 TCase("Hello!", (FgColor.GREEN, Format.BLINK),
                       "\033[0;32;5mHello!\033[0m"))

        for case in cases:
            got = esc_attrs(case.text, *case.attrs)
            self.assertEqual(got, case.want)

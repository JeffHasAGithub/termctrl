import unittest
from termctrl.attr import Attr, esc_attrs
from typing import NamedTuple


class TCase(NamedTuple):
    text: str
    attrs: tuple[Attr]
    want: str


class TestAttr(unittest.TestCase):
    def test_esc_attr(self):
        cases = {"empty_string": TCase("", (), "")}

        for case in cases.values():
            got = esc_attrs(case.text, *case.attrs)
            self.assertEqual(got, case.want)

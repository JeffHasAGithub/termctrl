import unittest
from termctrl.attr import esc_attrs


class TestAttr(unittest.TestCase):
    def test_esc_attr(self):
        got = esc_attrs("")
        self.assertEqual("", got)

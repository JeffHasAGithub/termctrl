import unittest
from termctrl.cursor import Position, parse_position
from termctrl.error import CursorError


class TestCursor(unittest.TestCase):
    def test_parse_position_valid(self):
        arg = "^[[37;1R"

        want = Position(37, 1)
        got = parse_position(arg)

        self.assertEqual(want.row, got.row)
        self.assertEqual(want.col, got.col)

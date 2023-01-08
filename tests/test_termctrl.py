import unittest
from collections import namedtuple
from termctrl.color import (FgColor, BgColor,
                            write_fg, write_bg)


class TestColor(unittest.TestCase):

    def test_write_fg(self):
        """Test color.write_fg"""

        TC = namedtuple("TC", "color input want")

        tt: dict = {
                "red_text": TC(FgColor.RED, "The text is red!",
                               "\33[31mThe text is red!\33[0m"),
                "blue_text": TC(FgColor.BLUE, "The text is blue!",
                                "\33[34mThe text is blue!\33[0m"),
                }

        for t in tt.values():
            got = write_fg(t.color, t.input)
            self.assertEqual(got, t.want)

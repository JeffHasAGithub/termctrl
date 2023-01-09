import unittest

import io
from termctrl import TermCtrl


class TestTermCtrl(unittest.TestCase):

    def test_write(self):

        cases = {"empty_string": "",
                 "hello_world": "Hello World!",
                 "multi_line": "first line\nsecond line",
                 }

        for name, text in cases.items():
            term = TermCtrl(io.StringIO())
            term.write(text)

            self.assertEqual(term.buffer.getvalue(), text)

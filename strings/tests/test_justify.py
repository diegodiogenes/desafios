import unittest

from aligner.base_aligner import BaseAligner
from aligner.justify_aligner import JustifyAligner
from tests.fixtures.defaults import default_input_string, test_output_string_justify


class TestJustify(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.justify = JustifyAligner(limit=109)

    def test_class_type(self):
        self.assertTrue(isinstance(self.justify, BaseAligner))

    def test_base_case(self):
        out_str = self.justify.align_text(default_input_string)
        self.assertEqual(out_str, test_output_string_justify)

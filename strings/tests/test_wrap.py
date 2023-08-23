import unittest

from wrapper.paragraph_wrapper import ParagraphWrapper
from tests.fixtures.defaults import test_output_string_wrap, default_input_string_wrap


class TestJustify(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.wrapper = ParagraphWrapper(limit=40)

    def test_class_type(self):
        self.assertTrue(isinstance(self.wrapper, ParagraphWrapper))

    def test_base_case(self):
        paragraphs = default_input_string_wrap.splitlines()
        output_paragraphs = [self.wrapper.wrap(paragraph) for paragraph in paragraphs]

        output_str = '\n'.join(output_paragraphs)

        self.assertEqual(output_str, test_output_string_wrap)

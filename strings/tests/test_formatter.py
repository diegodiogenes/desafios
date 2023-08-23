import unittest
from unittest.mock import mock_open

import mock

from aligner.justify_aligner import JustifyAligner
from formatter.formatter import Formatter
from tests.fixtures.defaults import default_input_string
from tests.mocks.file_system_mock import MockFileSystem
from wrapper.paragraph_wrapper import ParagraphWrapper


class TestFormatter(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.file_system = MockFileSystem('test')
        cls.wrapper = ParagraphWrapper(limit=40)
        cls.aligner = JustifyAligner(limit=40)

    @mock.patch('wrapper.paragraph_wrapper.ParagraphWrapper.wrap', return_value='')
    @mock.patch('aligner.justify_aligner.JustifyAligner.align_text', return_value='')
    @mock.patch('__main__.__builtins__.open', new_callable=mock_open)
    def test_base_case_all_methods_called(self, mock_file, mock_justify, mock_wrap):
        formatter = Formatter(input_str='test', wrapper=self.wrapper, aligner=self.aligner,
                              file_system=self.file_system)
        formatter.format(load_from_disk=True)

        mock_justify.assert_called_once()
        self.assertEqual(mock_wrap.call_count, len(default_input_string.splitlines()))
        mock_file.assert_called_once()
        mock_file.assert_called_with('outputs/test.txt', 'w+')

    @mock.patch('wrapper.paragraph_wrapper.ParagraphWrapper.wrap', return_value='')
    @mock.patch('aligner.justify_aligner.JustifyAligner.align_text', return_value='')
    @mock.patch('__main__.__builtins__.open', new_callable=mock_open)
    def test_base_case_dont_call_justify(self, mock_file, mock_justify, mock_wrap):
        formatter = Formatter(input_str='test', wrapper=self.wrapper, aligner=None, file_system=self.file_system)
        formatter.format(load_from_disk=True)

        mock_justify.asssert_not_called()
        self.assertEqual(mock_wrap.call_count, len(default_input_string.splitlines()))
        mock_file.assert_called_once()
        mock_file.assert_called_with('outputs/test.txt', 'w+')

    @mock.patch('tests.mocks.file_system_mock.MockFileSystem.read_file', return_value='')
    @mock.patch('wrapper.paragraph_wrapper.ParagraphWrapper.wrap', return_value='')
    @mock.patch('aligner.justify_aligner.JustifyAligner.align_text', return_value='')
    @mock.patch('__main__.__builtins__.open', new_callable=mock_open)
    def test_base_case_dont_read_from_file(self, mock_file, mock_justify, mock_wrap, mock_read_file):
        formatter = Formatter(input_str=default_input_string, wrapper=self.wrapper, aligner=self.aligner,
                              file_system=self.file_system)
        formatter.format()

        mock_read_file.asssert_not_called()
        self.assertEqual(mock_wrap.call_count, len(default_input_string.splitlines()))
        mock_justify.assert_called_once()
        mock_file.assert_called_once()
        mock_file.assert_called_with('outputs/test.txt', 'w+')

    @mock.patch('tests.mocks.file_system_mock.MockFileSystem.read_file')
    @mock.patch('wrapper.paragraph_wrapper.ParagraphWrapper.wrap', return_value='')
    @mock.patch('aligner.justify_aligner.JustifyAligner.align_text', return_value='')
    @mock.patch('__main__.__builtins__.open', new_callable=mock_open)
    def test_base_case_logs_error(self, mock_file, mock_justify, mock_wrap, mock_read_file):
        mock_read_file.side_effect = FileNotFoundError()
        with self.assertLogs(level=1) as logs:
            formatter = Formatter(input_str=default_input_string, wrapper=self.wrapper, aligner=self.aligner,
                                  file_system=self.file_system)
            formatter.format(load_from_disk=True)

            mock_wrap.assert_not_called()
            mock_justify.asssert_not_called()

        self.assertEqual('ERROR', logs.records[0].levelname)

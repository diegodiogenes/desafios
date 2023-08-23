import logging
from typing import List

from mixins.string_mixin import StringMixin
from aligner.base_aligner import BaseAligner
from wrapper.base_wrapper import BaseWrapper
from filesystem.file_system import FileSystem

logger = logging.Logger


class Formatter(StringMixin):
    """
    Formatter class to Wrap, Align and Save
    """
    def __init__(self, input_str: str, wrapper: BaseWrapper, file_system: FileSystem,
                 aligner: BaseAligner = None) -> None:
        """
        Class Constructor
        :param input_str: String input to open file or use to formatter
        :param wrapper: Wrapper implementation
        :param file_system: Filesystem implementation
        :param aligner: Aligner implementation
        """
        self.input_str = input_str
        self.wrapper = wrapper
        self.aligner = aligner
        self.file_system = file_system

    def _get_wrap_text(self, load_from_disk: bool = False) -> List[str]:
        """
        Private method to wrap each paragraph on string
        :param load_from_disk: Flag to indicate if string read from file or parameter
        :return: List of strings wrapped
        """
        if load_from_disk:
            return [self.wrapper.wrap(paragraph) for paragraph in
                    self.file_system.read_file(self.input_str)]

        return [self.wrapper.wrap(paragraph) for paragraph in
                self.extract_lines(self.input_str)]

    def format(self, load_from_disk: bool = False) -> str:
        """
        Format string with align and wrap
        :param load_from_disk: Flag to indicate if string read from file or parameter
        :return: Complete wrapped string
        """
        try:
            output_paragraphs = self._get_wrap_text(load_from_disk)
            output_str = '\n'.join(output_paragraphs)

            if self.aligner:
                output_str = self.aligner.align_text(output_str)

            self.file_system.write_file(output_str)
            return output_str
        except Exception as e:
            logging.error(e)

from typing import List


class StringMixin:
    """
    Mixin with manipulation string methods
    """
    @staticmethod
    def extract_lines(text: str) -> List[str]:
        """
        Split lines of string
        :param text: String to split lines
        :return:
        """
        return text.splitlines()

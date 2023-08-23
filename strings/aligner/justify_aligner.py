from typing import List, Tuple

from aligner.base_aligner import BaseAligner
from mixins.string_mixin import StringMixin

ONE_WORD = 1


class JustifyAligner(BaseAligner, StringMixin):
    """
    Class to justify text
    """

    def __init__(self, limit: int) -> None:
        super(JustifyAligner, self).__init__(limit)

    def align_text(self, text: str) -> str:
        """
        Align method to justify text
        :param text: text to justify
        :return: Aligned String
        """
        paragraphs = self.extract_lines(text)
        output_paragraphs = [self._justify_paragraph(paragraph) for paragraph in paragraphs]
        return '\n'.join(output_paragraphs)

    def _spaces_to_add(self, len_line: int, len_words: int) -> Tuple[int, int]:
        """
        Private method to calculate how many spaces to add between words to justify
        :param len_line: size of paragraph
        :param len_words: quantity of words on paragraph
        :return: Tuple with spaces to add between words and extra spaces
        """
        spaces_to_fill = self._limit - len_line
        spaces_between_words, extra_spaces = divmod(spaces_to_fill, (len_words - 1))
        return spaces_between_words, extra_spaces

    def _justify_line(self, words: List[str], spaces_between_words: int, extra_spaces: int) -> str:
        """
        Method to justify the line of paragraph
        :param words:
        :param spaces_between_words:
        :param extra_spaces:
        :return: Justified Line
        """
        justified_line = words[0]
        words_to_justify = words[1::]

        for word in words_to_justify:
            if extra_spaces > 0:
                justified_line += ' ' + ' ' * (spaces_between_words + 1) + word
                extra_spaces -= 1
            else:
                justified_line += ' ' + ' ' * spaces_between_words + word

        return justified_line

    def _justify_paragraph(self, paragraph: str) -> str:
        """
        Method to justify the paragraph
        :param paragraph: paragraph of the string
        :return: justified paragraph
        """
        words = paragraph.split()
        if len(words) <= ONE_WORD:
            return paragraph
        spaces_between_words, extra_spaces = self._spaces_to_add(len(paragraph), len(words))
        if any((spaces_between_words, extra_spaces)):
            return self._justify_line(words, spaces_between_words, extra_spaces)

        return paragraph

import textwrap

from mixins.string_mixin import StringMixin
from wrapper.base_wrapper import BaseWrapper


class ParagraphWrapper(BaseWrapper, StringMixin):
    """
    Paragraph Wrapper implementation
    """
    def __init__(self, limit: int):
        super(ParagraphWrapper, self).__init__(limit)

    def _wrap_paragraphs(self, paragraph) -> str:
        """
        Wrap paragraph text
        :param paragraph: Paragraph of text
        :return:
        """
        return '\n'.join(textwrap.wrap(paragraph, self.limit))

    def wrap(self, paragraph) -> str:
        return self._wrap_paragraphs(paragraph)

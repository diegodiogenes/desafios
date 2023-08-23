from abc import ABC, abstractmethod


class BaseAligner(ABC):
    """
    Base Aligner Class, interface that provides standard way to create
    new aligners such as Justify align, Center align, etc.
    """

    def __init__(self, limit: int = 40) -> None:
        """
        Class Constructor
        :param limit: line limit to align
        """
        self._limit = limit

    @abstractmethod
    def align_text(self, text: str) -> str:
        """
        Abstract method to implement on children class to align text
        :param text:
        :return: align string
        """
        pass

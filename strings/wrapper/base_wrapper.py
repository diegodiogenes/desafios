from abc import ABC, abstractmethod


class BaseWrapper(ABC):
    """
    Base class to standard methods to implement a String Wrapper
    """
    def __init__(self, limit: int) -> None:
        """
        Limit of string
        :param limit: int
        """
        self.limit = limit

    @abstractmethod
    def wrap(self, paragraph: str) -> str:
        pass

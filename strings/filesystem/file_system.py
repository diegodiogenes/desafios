from abc import ABC, abstractmethod
from typing import Generator


class FileSystem(ABC):
    """
    Base Classe to create filesystem with standards methods
    """

    def __init__(self, path: str) -> None:
        """
        Constructor that receive a path
        :param path: Path to read file
        """
        self.path: str = path

    @abstractmethod
    def write_file(self, output: str) -> None:
        """
        Abstract method to write a file
        :param output: string to write on file
        :return: None
        """
        pass

    @abstractmethod
    def read_file(self, name: str) -> Generator[str, None, None]:
        """
        Abstract method to read a file
        :param name: name of file to read
        :return: None
        """
        pass

import os.path
import uuid
from typing import Generator

from filesystem.file_system import FileSystem


class FileLocal(FileSystem):
    """
    Classe to manager local file system
    """
    dest_path = "outputs"

    def __init__(self, path: str = None):
        super(FileLocal, self).__init__(path)

    @classmethod
    def _get_absolute_name(cls) -> str:
        """
        Create A absolute name to write file
        :return: path and name of file
        """
        name = f"{uuid.uuid4()}.txt"
        return os.path.join(os.path.abspath(os.curdir), cls.dest_path, name)

    def write_file(self, output_str: str) -> None:
        """
        Write file on disk local
        :param output_str: string to write on file
        :return: None
        """
        with open(self._get_absolute_name(), "w+") as file:
            file.writelines(output_str)

    def read_file(self, name: str) -> Generator[str, None, None]:
        """
        Read a file on local system
        :param name: Name of file to read
        :return: Generator with line on file
        """
        with open(f"{self.path}/{name}") as file:
            lines = file.readlines()
            for line in lines:
                yield line

import unittest.mock

from filesystem.file_system import FileSystem
from tests.fixtures.defaults import default_input_string


class MockFileSystem(FileSystem):
    """
    Mock File System to use on tests
    """
    def write_file(self, output: str):
        with open('outputs/test.txt', 'w+') as f:
            f.writelines(output)

    def read_file(self, name: str):
        lines = default_input_string.splitlines()
        for line in lines:
            yield line

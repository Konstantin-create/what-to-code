from rich import print
from tools.sharing_file_tools import *
from tools.load_tools import *


class LoadCommand:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.mode = 'save'

    def from_path(self):
        """Function to load ideas from path"""

        pass

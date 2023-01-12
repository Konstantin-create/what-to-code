from rich import print
from config import Config


class SaveCommand:
    def __init__(self, save_path: str, header: str, body: str):
        self.save_path = save_path | Config.save_path
        self.header = header
        self.body = body

    def save_idea(self):
        """Function to save idea"""

        if not self.header and not self.body:
            print('[red]You can\'t save idea without header or body')
            return
        


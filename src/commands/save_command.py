from rich import print
from config import Config
from tools.save_tools import *


class SaveCommand:
    def __init__(self, header: str = '', body: str = ''):
        self.save_path = Config.save_path
        self.header = header
        self.body = body

    def save_idea(self):
        """Function to save idea"""

        if not self.header and not self.body:
            print('[red]You can\'t save idea without header or body')
            return
        save_responce = save_idea(header=self.header, body=self.body)
        if not save_responce:
            print(f"""
            [red]An error occured![/red]
            [yellow]For devs: {save_responce}[/yellow]
            """)
            return
        print(f"""[green]Idea were saved[/green]""")

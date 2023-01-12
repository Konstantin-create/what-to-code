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
        save_response = save_idea(header=self.header, body=self.body)
        print(save_response)
        if not save_response:
            print(f"""
            [red]An error occurred![/red]
            [yellow]For devs: {save_response}[/yellow]
            """)
            return
        print(f"""[green]Idea were saved[/green]""")

    def print_list(self):
        """Function to print list of ideas"""

        ideas = get_ideas_data()
        if not ideas:
            print('[yellow]Ideas were n\'t found[/yellow]'
                  'You haven\'t saved them yet, or a permissions error has occurred'
                  )
            return 
        for idea in ideas:
            print(f'    {idea["header"]}')
            print(f'    {idea["body"]}')

        print(f'[green]Total: {len(ideas)}[/green]')

from rich import print
from tools.save_tools import save_idea
from tools.sharing_file_tools import *


class LoadCommand:
    def __init__(self, file_path: str, autosave: bool = False):
        self.file_path = file_path
        self.mode = 'save'
        self.autosave = autosave

    def by_path(self):
        """Function to load ideas from path"""

        print(f'[green]Load from file "{self.file_path}"[/green]')
        file_data = load_wtc_file(path=self.file_path)
        print(f'[yellow]Computer name: {file_data["pc_name"]}[/yellow]')
        print(f'[yellow]Time stamp: {file_data["pc_timestamp"]}[/yellow]')
        print()
        print()
        print(f'[green]Found: {file_data["ideas_amount"]} ideas[/green]')
        if not self.autosave:
            command = input('Save ideas to local storage(y/N): ').strip().lower()
            if command != 'y':
                print()
                print('[red]Ideas were n\'t saved[/red]')
                return
        for idea in file_data['ideas']:
            if not save_idea(header=idea['header'], body=idea['body']):
                print(f'[yellow]You already have "{idea["header"]}" in your local storage[/yellow]')
                continue
            print(f'Success: save "{idea["header"]}"')

        print()
        print(f'[green]{file_data["ideas_amount"]} ideas were added[/green]')

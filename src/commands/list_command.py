from rich import print
from config import Config


class ListCommand:
    def list_of_sources(self):
        """Function to print list of sources"""

        print('[green]Sources[/green]')
        urls = Config.urls
        for i in range(len(urls)):
            print(f'    {i} - {urls[i]}')
        print()
        print(f'[yellow]Total: {len(urls)}[/yellow]')

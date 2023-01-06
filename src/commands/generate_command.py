import random
from rich import print
from config import Config
from tools.parse_ideas import *
from tools.tools import ParseResponse


class GenerateCommand:
    def __init__(self, source_all: bool = True, source: int = -1):
        self.source_all = source_all
        self.source = source

    def generate_idea(self) -> ParseResponse:
        """Function to generate list of ideas from different services"""

        if self.source_all:
            ideas = parse()
        else:
            ideas = parse(parse_all=False, index=self.source)
        return random.choice(ideas)

    def print(self):
        """Function to print idea"""

        idea = self.generate_idea()
        if idea.code == 100:
            print(
                f"""
        [green]Idea were generated![/green]
        
        [yellow]{idea.header}[/yellow]
        {idea.body}
                """
            )
        elif idea.code == 200:
            print('[red]En server error occurred[/red]')
        elif idea.code == 300:
            print('[red]En error occurred[/red]')
        elif idea.code == 400:
            print('[red]Internet connection error occurred. Check connection!')

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
        if idea.error == 100:
            print(
                f"""
    [green]Idea were generated![/green]
        
    [yellow]{idea.header}[/yellow]
    {idea.body}
    """)
        elif idea.error == 200:
            print('[red]En server error occurred[/red]')
        elif idea.error == 300:
            print('[red]En error occurred[/red]')
        elif idea.error == 400:
            print('[red]Internet connection error occurred. Check connection!')
    
    def generate_list(self, emount: int) -> list:
        """Function to generate list of ideas"""

        ideas = []
        for _ in range(emount):
            idea = self.generate_idea()
            while idea.error != 100:
                idea = self.generate_idea()
            ideas.append(idea)

    def print_list(self, emount: int) -> None:
        """Function to print list of ideas"""

        ideas = self.generate_list(emount)
        for idea in ideas:
            if idea.error == 100:
                print(
                f"""
    [green]Idea were generated![/green]
        
    [yellow]{idea.header}[/yellow]
    {idea.body}
    """)

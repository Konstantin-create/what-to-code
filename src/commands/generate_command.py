import random
from rich import print
from tools.parse_ideas import *
from tools.tools import ParseResponse


class GenerateCommand:
    def __init__(self, source_all: bool = True, source: str = ''):
        self.source_all = source_all
        self.source = source

    def generate_idea(self) -> ParseResponse:
        """Function to generate list of ideas from different services"""

        ideas = [parse_w_t_c()]
        return random.choice(ideas)

    def print(self):
        """Function to print idea"""

        idea = self.generate_idea()
        print(
            f"""
    [green]Idea were generated![/green]
    
    [yellow]{idea.header}[/yellow]
    {idea.body}
            """
        )

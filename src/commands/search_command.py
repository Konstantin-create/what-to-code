from rich import print
from tools.search_tools import *
from tools.save_tools import get_ideas_data, get_idea_by_id


class SearchCommand:
    def __init__(self):
        pass

    def by_string(self, string_to_find: str) -> dict:
        """Function to find idea by part of header/data"""

        ideas = get_ideas_data()
        ideas_out = {}

        for i in range(len(ideas)):
            ideas_out[i] = max(compare_strings(needle=string_to_find, hay=ideas[i]['header']),
                               compare_strings(needle=string_to_find, hay=ideas[i]['body']))

        return ideas_out

    def approximate_search_by_string(self, string_to_find: str) -> None:
        """Function to print search result of approximate search"""

        ideas_weights = self.by_string(string_to_find)
        top_idea_id = max(ideas_weights, key=lambda idea: ideas_weights[idea])

        if ideas_weights[top_idea_id] == 0:
            print('[red]Idea were n\'t found[/red]')
            return
        if ideas_weights[top_idea_id] <= 0.6:
            print('[yellow]The most similar ideas ideas were found[/yellow]')
        else:
            print('[green]The most similar idea[/green]')
        idea = get_idea_by_id(top_idea_id)
        print(f'[yellow]Idea ID: {top_idea_id}[/yellow]')
        print(f'    {idea["header"]}')
        print(f'    {idea["body"]}')

    def search_by_id(self, id_to_find: int):
        """Function t oprint search result by saved idea id"""

        idea = get_idea_by_id(id_to_find)
        if not idea['header'] and not idea['body']:
            print('[red]Idea were n\'t found[/red]')
            return

        print(f'[yellow]Idea ID: {id_to_find}[/yellow]')
        print(f'    {idea["header"]}')
        print(f'    {idea["body"]}')

    def print_list(self):
        """Function to print list of ideas"""

        ideas = get_ideas_data()
        if not ideas:
            print('[yellow]Ideas were n\'t found[/yellow]'
                  'You haven\'t saved them yet, or a permissions error has occurred'
                  )
            return
        for i in range(len(ideas)):
            print(f'[yellow]Idea ID: {i}[/yellow]')
            print(f'    {ideas[i]["header"]}')
            print(f'    {ideas[i]["body"]}')
            print()

        print(f'[green]Total: {len(ideas)}[/green]')

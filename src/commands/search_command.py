from tools.search_tools import *
from tools.save_tools import get_ideas_data


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

    def print_search_results(self, string_to_find: str) -> None:
        """Function to print search result of approximate search"""

        ideas_weights = self.by_string(string_to_find)
        top_idea_id = max(ideas_weights, key=lambda idea: ideas_weights[idea])

        if ideas_weights[top_idea_id] == 0:
            print('[red]Idea were n\'t found[/red]')
            return
        if ideas_weights[top_idea_id] <= 0.5:
            print('[yellow]Similar ideas were n\'t found')
        print(ideas_weights)

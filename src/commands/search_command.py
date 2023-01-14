from tools.search_tools import *
from tools.save_tools import get_ideas_data


class SearchCommand:
    def __init__(self):
        pass

    def by_string(self, string_to_find: str):
        """Function to find idea by part of header/data"""

        ideas = get_ideas_data()
        ideas_out = []

        for i in range(len(ideas)):
            ideas_out.append({
                i: {
                    'header': compare_strings(needle=string_to_find, hay=ideas[i]['header']),
                    'body': compare_strings(needle=string_to_find, hay=ideas[i]['body'])
                }
            })

        print(ideas_out)

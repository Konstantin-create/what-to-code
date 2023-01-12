from typing import Union

import os
import json
from config import Config

user_path = os.path.expanduser("~")


def create_base_structure() -> Union[True, Exception]:
    """Function to create base structure of .what-to-code folder"""

    config_data = {
        'save_path': '~/.what-to-code'
    }

    try:
        if not os.path.exists('~/.what-to-code'):
            os.mkdir('~/.what-to-code')
        if not os.path.exists(f'{user_path}/.what-to-code/config.json'):
            json.dump(open(f'{user_path}/.what-to-code/config.json', 'w'), config_data)
        if not os.path.exists(f'{user_path}/.what-to-code/ideas.json'):
            json.dump(open(f'{user_path}/.what-to-code/ideas.json', 'w'), [])
    except Exception as e:
        return e


def save_idea(header: str, body: str) -> Union[True, Exception]:
    """Function to save idea in .what-to-code/ideas.json"""

    create_base_structure()

    current_ideas = json.load(open(f'{user_path}//.what-to-code/ideas.json', 'r'))
    current_ideas.append({'header': header, 'body': body})
    try:
        json.dump(open(f'{user_path}//.what-to-code//ideas.json', 'w'), current_ideas)
        return True
    except Exception as e:
        return e

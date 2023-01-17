from typing import Union

import os
import json
from config import Config

user_path = os.path.expanduser("~")
default_config_data = {
    'save_path': '~/.what-to-code'
}


def create_base_structure() -> Union[bool, Exception]:
    """Function to create base structure of .what-to-code folder"""

    try:
        if not os.path.exists(f'{user_path}/.what-to-code'):
            os.mkdir(f'{user_path}/.what-to-code')
            print('created')
        if not os.path.exists(f'{user_path}/.what-to-code/config.json'):
            json.dump(default_config_data, open(f'{user_path}/.what-to-code/config.json', 'w'), indent=2)
        if not os.path.exists(f'{user_path}/.what-to-code/ideas.json'):
            json.dump([], open(f'{user_path}/.what-to-code/ideas.json', 'w'), indent=2)
        return True
    except Exception as e:
        return e


def get_config_data() -> dict:
    """Function to get config data from .what-to-code/config.json"""

    try:
        return json.load(open(f'{user_path}/.what-to-code/config.json', 'r'))
    except:
        return default_config_data


def get_ideas_data() -> list:
    """Function to get list of ideas"""

    try:
        return json.load(open(f'{user_path}/.what-to-code/ideas.json', 'r'))
    except:
        return []


def get_idea_by_id(idea_id: int) -> dict:
    """Function to get idea by id"""

    ideas = get_ideas_data()
    try:
        return ideas[idea_id]
    except:
        return {'header': '', 'body': '[red]An idea were n\'t found[/red]'}


def save_idea(header: str, body: str) -> Union[bool, Exception]:
    """Function to save idea in .what-to-code/ideas.json"""

    response = create_base_structure()
    if not response:
        return response

    current_ideas = json.load(open(f'{user_path}//.what-to-code/ideas.json', 'r'))
    current_ideas.append({'header': header, 'body': body})
    try:
        json.dump(current_ideas, open(f'{user_path}//.what-to-code//ideas.json', 'w'), indent=2)
        return True
    except Exception as e:
        return e

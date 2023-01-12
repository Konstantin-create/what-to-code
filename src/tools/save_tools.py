from typing import Union

import os
import json
from config import Config


user_path = os.path.expanduser("~")

def check_folder() -> bool:
    """Function to check is .what-to-code folder"""

    return os.path.exists(Config.save_path)

def create_folder() -> None:
    """Function to create .what-to-code folder"""


    if not check_folder:
        os.mkdir(f'{user_path}//.what-to-code')

def save_idea(header: str, body: str) -> Union[True, Exception]:
    """Function to save idea in .what-to-code/ideas.json"""

    
    create_folder()

    if f'{user_path}//.what-to-code//ideas.json':
        current_ideas = json.load(open(f'{user_path}//.what-to-code/ideas.json', 'r'))
    current_ideas = []
    current_ideas.append({'header': header, 'body': body})
    try:
        json.dump(open(f'{user_path}//.what-to-code//ideas.json', 'w'), current_ideas)
        return True
    except Exception as e:
        return e

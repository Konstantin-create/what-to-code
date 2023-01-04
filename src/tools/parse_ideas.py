import json
import random
import requests
from bs4 import BeautifulSoup

from config import Config
from .tools import ParseResponse


def parse(parse_all=True, index: int = -1) -> list:
    """Function to get ideas from different services"""

    if parse_all:
        out = [parse_w_t_c(), parse_ideasai()]
        return out

    if index > len(Config.urls):
        return [ParseResponse(error=400), ]
    try:
        site = list(Config.api_urls.keys())[index]
        if site == 'what_to_code':
            return [parse_w_t_c(), ]
        if site == 'ideasai':
            return [parse_ideasai(), ]
    except:
        return [ParseResponse(error=400), ]


def parse_w_t_c() -> ParseResponse:
    """Function to get idea from https://what-to-code.com"""

    page = requests.get(Config.api_urls['what_to_code'])
    data = json.loads(page.text)
    data['title'].capitalize()
    data['description'].capitalize().replace('\n', '')
    return ParseResponse(header=data['title'], body=data['description'], error=100)


def parse_ideasai() -> ParseResponse:
    """Function to parse https://ideasai.com/"""

    page = requests.get(Config.api_urls['ideasai'])
    soup = BeautifulSoup(page.text, 'html.parser')
    idea = random.choice(soup.find_all('h3')).text
    return ParseResponse(header='From GPT-3', body=idea, error=100)

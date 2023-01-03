import json
import requests

from config import Config
from .tools import ParseResponse


def parce(parce_all=True, index: int = -1) -> list:
    """Function to get ideas from different servises"""

    if parce_all:
        out = [parse_w_t_c()]
        return out

    if index > len(Config.urls):
        return [ParseResponse(error=400)]
    try:
        site = Config.api_urls.keys()[index]
        if site == 'https://what-to-code.com':
            return [parse_w_t_c(), ]
    except:
        return [ParseResponse(error=400)]


def parse_w_t_c() -> ParseResponse:
    """Function to get idea from https://what-to-code.com"""

    page = requests.get(Config.api_urls['what_to_code'])
    data = json.loads(page.text)
    data['title'].capitalize()
    data['description'].capitalize().replace('\n', '')
    return ParseResponse(header=data['title'], body=data['description'], error=100)

def parse_codepen_io() -> ParseResponse:
    """Function to parse https://codepen.io/26pierrek/full/zYoWYjv"""

    page = requests.get(Config.api_urls['codepen_io'])
    print(page.text)

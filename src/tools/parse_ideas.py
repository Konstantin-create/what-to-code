import json
import requests

from config import Config
from .tools import ParseResponse


def parse_w_t_c():
    """Function to get idea from https://what-to-code.com"""

    page = requests.get(Config.api_urls['what_to_code'])
    data = json.loads(page.text)
    data['title'].capitalize()
    data['description'].capitalize().replace('\n', '')
    return ParseResponse(header=data['title'], body=data['description'], error=100)

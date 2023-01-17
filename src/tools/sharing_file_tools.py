import os


def parse_file_data(file_data: sting) -> dict:
    """Function to convert file data string to dict"""

    pass


def load_wtc_file(path: str) -> dict:
    """Function to load .wtc file"""

    if not os.path.exists(path):
        return {'error': 'File not exists'}

    with open(path, 'r') as file:
        file_data = file.read()

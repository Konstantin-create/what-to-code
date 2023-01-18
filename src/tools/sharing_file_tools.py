import os


def parse_file_data(file_data: str) -> dict:
    """Function to convert file data string to dict"""

    parsed_data = {}

    for data_line in file_data:
        if '[PC_NAME]' in data_line:
            parsed_data['pc_name'] = data_line[data_line.find('[PC_NAME]') + 9:data_line.find('[/PC_NAME]')]
        if '[PC_TIMESTAMP]' in data_line:
            parsed_data['pc_timestamp'] = data_line[
                                          data_line.find('[PC_TIMESTAMP]') + 14:data_line.find('[/PC_TIMESTAMP]')
                                          ]
        if '[IDEAS]' in data_line:
            parsed_data['ideas'] = []
            while '[/IDEAS]' not in data_line:
                if '[IDEA]' in data_line:
                    while '[/IDEA]' not in data_line:
                        break

    print(parsed_data)


def load_wtc_file(path: str) -> dict:
    """Function to load .wtc file"""

    if not os.path.exists(path):
        return {'error': 'File not exists'}

    with open(path, 'r') as file:
        file_data = file.readlines()
    parse_file_data(file_data)

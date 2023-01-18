import os


def parse_file_data(file_data: str) -> dict:
    """Function to convert file data string to dict"""

    parsed_data = {}
    in_idea_block = False
    in_ideas_block = False
    tmp_idea = {}

    for data_line in file_data:
        data_line = data_line.strip()
        if in_ideas_block:
            if '[IDEA]' in data_line:
                in_idea_block = True
            elif '[/IDEA]' in data_line:
                in_idea_block = False
                parsed_data['ideas'].append(tmp_idea)
                tmp_idea = {}
            if in_idea_block:
                if '[HEADER]' in data_line:
                    tmp_idea['header'] = data_line[data_line.find('[HEADER]') + 8:data_line.find('[/HEADER]')]
                if '[BODY]' in data_line:
                    tmp_idea['body'] = data_line[data_line.find('[BODY]') + 6:data_line.find('[/BODY]')]

        if '[PC_NAME]' in data_line:
            parsed_data['pc_name'] = data_line[data_line.find('[PC_NAME]') + 9:data_line.find('[/PC_NAME]')]
        elif '[PC_TIMESTAMP]' in data_line:
            parsed_data['pc_timestamp'] = data_line[
                                          data_line.find('[PC_TIMESTAMP]') + 14:data_line.find('[/PC_TIMESTAMP]')]
        elif '[IDEAS_EMOUT]' in data_line:
            parsed_data['ideas_emout'] = data_line[
                                         data_line.find('[IDEAS_EMOUT]') + 12:data_line.find('[/IDEAS_EMOUT]')]
        elif '[IDEAS]' in data_line:
            parsed_data['ideas'] = []
            in_ideas_block = True

    return parsed_data


def load_wtc_file(path: str) -> dict:
    """Function to load .wtc file"""

    if not os.path.exists(path):
        return {'error': 'File not exists'}

    with open(path, 'r') as file:
        file_data = file.readlines()
    print(parse_file_data(file_data))

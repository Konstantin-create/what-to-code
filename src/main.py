# Parsers import
from parsers.parser import parser

# Base structure creator import
from tools.save_tools import create_base_structure

if __name__ == '__main__':
    create_base_structure()
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)

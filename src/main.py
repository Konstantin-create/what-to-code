# Parsers import
from parsers.parser import parser

# Config import

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)

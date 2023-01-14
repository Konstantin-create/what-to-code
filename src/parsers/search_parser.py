from .parser import subparsers
from argparse import Namespace


def search_handler(args: Namespace):
    pass


# Find parser
find_parser = subparsers.add_parser('search', help='command to find idea in saved ideas')
find_parser.set_deffaults(func=search_handler)

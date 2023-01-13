from .parser import subparsers
from argparse import Namespace


def find_handler(args: Namespace):
    pass


# Find parser
find_parser = subparsers.add_parser('save', help='command to find idea in saved ideas')
find_parser.set_deffaults(func=find_handler)

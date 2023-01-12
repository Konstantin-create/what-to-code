from .parser import subparsers
from argparse import Namespace


def save_handler(args: Namespace):
    """Handler for save command"""

    pass


# Save parser
save_parser = subparsers.add_parser('save', help='Command to save your code ideas')
save_parser.set_defaults(func=save_handler)

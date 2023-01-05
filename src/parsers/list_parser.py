from .parser import subparsers
from argparse import Namespace
from commands import ListCommand


def list_handler(args: Namespace):
    """Handler for list command"""

    list_command = ListCommand()
    list_command.list_of_sources()


# List parser
list_parser = subparsers.add_parser('list', help='Command to print list of sources')

list_parser.set_defaults(func=list_handler)

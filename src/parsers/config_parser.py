from .parser import subparsers
from argparse import Namespace
from commands import ConfigCommand


def config_handler(args: Namespace):
    pass


# Config parser
config_parser = subparsers.add_parser('config', help='Command to save new config data')
config_parser.set_defaults(func=config_handler)

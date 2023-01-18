import os.path

from .parser import subparsers
from argparse import Namespace


def load_handler(args: Namespace):
    if not os.path.exists(args.file_path):
        print(f'[red]"{args.file_path}" - does n\'t exists[/red]')
        return
    # todo: load command


# Load parser
load_parser = subparsers.add_parser('load', help='command to load ideas from any .wtc file')
load_parser.add_argument(
    '-p', '--path',
    dest='file_path',
    default='',
    type=str,
    help='path to ideas .wtc file'
)

load_parser.set_defaults(func=load_handler)

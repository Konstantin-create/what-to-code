import os.path
from .parser import subparsers
from argparse import Namespace
from commands import LoadCommand


def load_handler(args: Namespace):
    if not os.path.exists(args.file_path.strip()):
        print(f'[red]"{args.file_path.strip()}" - does n\'t exists[/red]')
        return
    load_command = LoadCommand(file_path=args.file_path.strip(), autosave=args.autosave)
    load_command.by_path()


# Load parser
load_parser = subparsers.add_parser('load', help='command to load ideas from any .wtc file')
load_parser.add_argument(
    '-p', '--path',
    dest='file_path',
    default='',
    type=str,
    help='path to ideas .wtc file'
)
load_parser.add_argument(
    '-y', '--yes',
    dest='auto_save',
    action='store_true',
    help='auto save ideas from .wtc file'
)

load_parser.set_defaults(func=load_handler)

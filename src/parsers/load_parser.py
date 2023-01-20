import os.path
from .parser import subparsers
from argparse import Namespace
from commands import LoadCommand


def load_handler(args: Namespace):
    if not os.path.exists(args.file_path.strip()):
        print(f'[red]"{args.file_path.strip()}" - does n\'t exists[/red]')
        return
    load_command = LoadCommand(file_path=args.file_path.strip(), autosave=args.autosave)
    if args.show_ideas:
        load_command.show_ideas()
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
    dest='autosave',
    action='store_true',
    help='auto save ideas from .wtc file'
)

load_parser.add_argumnt(
    '-s', '--show',
    dest='show_ideas',
    action='store_true',
    help='show list of ideas in file without saving'
)

load_parser.set_defaults(func=load_handler)

from rich import print
from .parser import subparsers
from argparse import Namespace
from commands import SaveCommand


def save_handler(args: Namespace):
    """Handler for save command"""

    if args.load_from_file:
        # todo: load from file
        return

    if args.add_list:
        print(f'[green]Adding {args.add_list} ideas[/green]')
        for i in range(args.add_list):
            print(f'Add {i + 1} idea')
            header = input('    Idea header: ')
            body = input('    Idea body: ')
            save_obj = SaveCommand(header=header, body=body)
            save_obj.save_idea()
            print('[yellow]Idea were added[/yellow]')
        return

    header = input('    Idea header: ')
    body = input('    Idea body: ')
    save_obj = SaveCommand(header=header, body=body)
    save_obj.save_idea()


# Save parser
save_parser = subparsers.add_parser('save', help='Command to save your code ideas')
save_parser.add_argument(
    '-l', '--list',
    dest='add_list',
    type=int,
    help='command to save list of ideas'
)

save_parser.add_argument(
    '-f', '--file',
    dest='load_from_file',
    action='store_true',
    help='command to load ideas list from custom file'
)

save_parser.set_defaults(func=save_handler)

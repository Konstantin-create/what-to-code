from .parser import subparsers
from argparse import Namespace
from commands import SaveCommand


def save_handler(args: Namespace):
    """Handler for save command"""

    if args.add_list:
        print(f'[green]Adding {args.add_list} ideas')
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

save_parser.set_defaults(func=save_handler)

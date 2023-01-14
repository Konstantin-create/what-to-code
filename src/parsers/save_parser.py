from .parser import subparsers
from argparse import Namespace
from commands import SaveCommand


def save_handler(args: Namespace):
    """Handler for save command"""

    if args.print_list:
        SaveCommand().print_list()
        return
    header = input('    Idea header: ')
    body = input('  Idea body: ')
    save_obj = SaveCommand(header=header, body=body)
    save_obj.save_idea()


# Save parser
save_parser = subparsers.add_parser('save', help='Command to save your code ideas')

save_parser.add_argument(
    '-l', '--list',
    dest='print_list',
    action='store_true',
    help='command to print list of saved ideas'
)

save_parser.set_defaults(func=save_handler)

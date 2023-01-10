from .parser import subparsers
from argparse import Namespace
from commands import GenerateCommand


def generate_handler(args: Namespace):
    """Handler for generate command"""

    idea = GenerateCommand()

    if args.print_list != -1:
        idea.print_list(emount=10)
    if args.source != -1:
        idea = GenerateCommand(source_all=False, source=args.source)

    idea.print()


# Generate parser
generate_parser = subparsers.add_parser('generate', help='Command to generate random idea from source')

generate_parser.add_argument(
    '-A', '--all',
    dest='source_all',
    default=True,
    action='store_true',
    help='command to generate idea from all source'
)

generate_parser.add_argument(
    '-s', '--source',
    dest='source',
    type=int,
    default=-1,
    help='command to generate idea from source'
)

generate_parser.add_argument(
    '-l', '--list',
    default=-1,
    dest='print_list',
    help='command to generate list of ideas'
)

generate_parser.set_defaults(func=generate_handler)

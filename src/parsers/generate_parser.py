from .parser import subparsers
from argparse import Namespace
from commands import GenerateCommand


def generate_handler(args: Namespace):
    """Handler for generate command"""

    idea = GenerateCommand()
    if args.source_all:
        idea.source_all = True
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

generate_parser.set_defaults(func=generate_handler)

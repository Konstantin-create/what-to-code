from .parser import subparsers
from argparse import Namespace


def generate_handler(args: Namespace):
    """Handler for generate command"""

    if args.source_all:
        print('All')


# Generate parser
generate_parser = subparsers.add_parser('generate', help='Command to generate random idea from source')

generate_parser.add_argument(
    '-A', '--all',
    dest='source_all',
    action='store_true',
    help='command to generate idea from all source'
)

generate_parser.set_defaults(func=generate_handler)

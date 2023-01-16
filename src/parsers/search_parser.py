from .parser import subparsers
from argparse import Namespace
from commands import SearchCommand


def search_handler(args: Namespace):
    search_obj = SearchCommand()
    if args.find_by_string:
        search_obj.approximate_search_by_string(string_to_find=args.find_by_string)
        return

    if args.find_by_id:
        search_obj.search_by_id(idea_id=args.find_by_id)
        return 


# Find parser
search_parser = subparsers.add_parser('search', help='command to find idea in saved ideas')
search_parser.add_argument(
    '-s', '--string',
    dest='find_by_string',
    type=str,
    help='command to find saved idea by part of header/body'
)

search_parser.add_argument(
    '-i', '--id',
    dest='find_by_id',
    type=int,
    help='command to find saved idea by id'
)

search_parser.set_defaults(func=search_handler)

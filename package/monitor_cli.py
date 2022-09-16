import argparse
#from resources import network

def cli():
    parser = argparse.ArgumentParser(
    description='Simple Python Resource Monitor',
    prog='monitor.py',
    usage='%(prog)s [RESOURCE] [OPTIONS]',
    epilog='Pass the resource along with -h flag to view list of resource options')

    subparser = parser.add_subparsers(
    dest='resource', 
    required=True)

    cpu_parser = subparser.add_parser(
    'cpu', 
    help='Display CPU Information')

    network_parser = subparser.add_parser(
    'network',
    help='Display network Information', 
    usage='monitor.py network [OPTIONS]')
    network_parser.add_argument(
    '-i',
    '--interface',
    help='Display interface addreses', 
    action='store_true')

    memory_parser = subparser.add_parser(
    'memory', 
    help='Display memory Information')

    disk_parser = subparser.add_parser(
    'disk', 
    help='Display disk Information')

    process_parser = subparser.add_parser(
    'process',
    usage='monitor.py process [OPTION]', 
    help='Display process Information')
    process_parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Display extended process information'
    )

    args = parser.parse_args()
    return vars(args)
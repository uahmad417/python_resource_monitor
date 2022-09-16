import argparse

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
        usage='monitor.py cpu [OPTIONS]',
        description='Displays CPU related information such as the seconds the CPU has spent in the given mode, processor count, percentage usage and CPU frequency',
        help='Display CPU Information')

    network_parser = subparser.add_parser(
        'network',
        help='Display network Information',
        description='Without any options, displays system-wide socket connections',
        usage='monitor.py network [OPTIONS]')
    network_parser.add_argument(
        '-i',
        '--interface',
        help='Display interface addresses', 
        action='store_true')

    memory_parser = subparser.add_parser(
        'memory',
        description='Displays statistics about system and swap memory usage',
        usage='monitory.py memory [-h]', 
        help='Displays system memory Information')

    disk_parser = subparser.add_parser(
        'disk',
        usage='monitory.py disk [OPTIONS]',
        description='Without any options, gives summary of mounted drives and filesystems', 
        help='Display disk Information')
    disk_parser.add_argument(
        '-p',
        '--partition',
        help='Displays all mounted disk partitions',
        action='store_true'
    )
    disk_parser.add_argument(
        '-u',
        '--usage',
        help='Displays disk usage statistics about partitions',
        action='store_true'
    )

    process_parser = subparser.add_parser(
        'process',
        usage='monitor.py process [OPTION]',
        description='Displays running ', 
        help='Display process Information about running process')
    process_parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Displays extended process information'
    )
    return vars(parser.parse_args())
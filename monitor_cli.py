import argparse

parser = argparse.ArgumentParser(description='Simple Python Resource Monitor',
                                prog='monitor',
                                usage='%(prog)s [RESOURCE] [OPTIONS]',
                                epilog='Pass the resource along with -h flag to view list of resource options')

subparser = parser.add_subparsers(dest='resource', required=True)

cpu_parser = subparser.add_parser('cpu', help='Display CPU Information')

network_parser = subparser.add_parser('network', help='Display network Information', usage='monitor network [OPTIONS]')
network_parser.add_argument('-i','--int',help='Display interface addreses', action='store_true')
memory_parser = subparser.add_parser('memory', help='Display memory Information')
disk_parser = subparser.add_parser('disk', help='Display disk Information')
process_parser = subparser.add_parser('process', help='Display process Information')


args = parser.parse_args()
print(vars(args))
from socket import AF_INET, socket
from socket import SOCK_DGRAM
from socket import SOCK_STREAM
from socket import AF_INET6


PROTOCOL_MAP = {
        (AF_INET, SOCK_STREAM): 'tcp',
        (AF_INET6, SOCK_STREAM): 'tcp6',
        (AF_INET, SOCK_DGRAM): 'udp',
        (AF_INET6, SOCK_DGRAM): 'udp6',
    }

NETSTAT_OUTPUT_FORMAT = '{:<10}{:<35}{:<20}{:<15}{:<15}'

IPCONFIG_OUTPUT_FORMAT ='\
    Physical Address: {:<15}\n\
    IPv4 Address: {:<15}\n\
    Subnet Mask: {:<15}\n\
    IPv6 Address: {:<15}'

from resources import network
FUNCTION_MAP = {
    'network': network.ipconfig if args.int else network.netstat
}

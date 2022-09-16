from ctypes.wintypes import PSHORT
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

PS_OUTPUT_FORMAT = '{:<10}{:<30}{:<15}{:<}'
PS_OUTPUT_FORMAT_VERBOSE = '{:<25}{:<10}{:<35}{:<10}{:<10}{:<10}{:15}{:<}'

'''CPU_OUTPUT_FORMAT = '\
    Platform: {:>15}\n\
    CPU(s): {:>15}\n\
    Thread(s) per core: {:>15}\n\
    Core(s) per socket: {:>15}\n\
    CPU MHz: {:>15}\n\
    Usage(%): {:>15}\n\
    CPU Times (user): {:>15.2f}\n\
    CPU Times (system): {:>15.2f}\n\
    CPU Times (idle): {:>15.2f}' '''
CPU_OUTPUT_FORMAT = '\
    {:<20}: {:>}\n\
    {:<20}: {:>}\n\
    {:<20}: {:>}\n\
    {:<20}: {:>}\n\
    {:<20}: {:>}\n\
    {:<20}: {:>}\n\
    {:<20}: {:>.2f}\n\
    {:<20}: {:>.2f}\n\
    {:<20}: {:>.2f}'     
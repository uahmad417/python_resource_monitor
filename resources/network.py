from xml.dom.pulldom import PROCESSING_INSTRUCTION
import psutil
from socket import AF_INET, socket
from socket import SOCK_DGRAM
from socket import SOCK_STREAM
from socket import AF_INET6

def netstat():
    protocol_map = {
        (AF_INET, SOCK_STREAM): 'tcp',
        (AF_INET6, SOCK_STREAM): 'tcp6',
        (AF_INET, SOCK_DGRAM): 'udp',
        (AF_INET6, SOCK_DGRAM): 'udp6',
    }

    network_output_format = '{:<10}{:<35}{:<20}{:<15}{:<15}'
    print(network_output_format.format('Proto','Local Address','Foreign Address','State','PID'))

    processes = {proc.info['pid']: proc.info['name'] for proc in psutil.process_iter(['pid','name'])}
    for socket_ in psutil.net_connections():
        protocol = protocol_map[(socket_.family,socket_.type)]
        local_address = f'{socket_.laddr.ip}:{socket_.laddr.port}'
        remote_address = f'{socket_.raddr.ip}:{socket_.raddr.port}' if socket_.raddr else '0.0.0.0:0'
        state = socket_.status
        pid_process_name = f'{socket_.pid}/{processes.get(socket_.pid)}'
        print(network_output_format.format(protocol,local_address,remote_address,state,pid_process_name))
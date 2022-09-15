import psutil
from package.resources.constants import PROTOCOL_MAP, NETSTAT_OUTPUT_FORMAT, IPCONFIG_OUTPUT_FORMAT

def netstat():
    print(NETSTAT_OUTPUT_FORMAT.format('Proto','Local Address','Foreign Address','State','PID'))
    processes = {proc.info['pid']: proc.info['name'] for proc in psutil.process_iter(['pid','name'])}
    for socket_ in psutil.net_connections():
        protocol = PROTOCOL_MAP[(socket_.family,socket_.type)]
        local_address = f'{socket_.laddr.ip}:{socket_.laddr.port}'
        remote_address = f'{socket_.raddr.ip}:{socket_.raddr.port}' if socket_.raddr else '0.0.0.0:0'
        state = socket_.status
        pid_process_name = f'{socket_.pid}/{processes.get(socket_.pid)}'
        print(NETSTAT_OUTPUT_FORMAT.format(protocol,local_address,remote_address,state,pid_process_name))

def ifconfig():
    return

def ipconfig():
    interface_info = psutil.net_if_addrs()
    
    for interface in interface_info:
        print('\n'+interface+'\n')
        mac_address = interface_info[interface][0].address if len(interface_info[interface]) == 3 else ''
        ipv4_address = interface_info[interface][1].address if len(interface_info[interface]) == 3 else interface_info[interface][0].address
        netmask = interface_info[interface][1].netmask if len(interface_info[interface]) == 3 else interface_info[interface][0].address
        ipv6_address = interface_info[interface][2].address if len(interface_info[interface]) == 3 else interface_info[interface][1].address
        print(IPCONFIG_OUTPUT_FORMAT.format(mac_address,ipv4_address,netmask,ipv6_address))
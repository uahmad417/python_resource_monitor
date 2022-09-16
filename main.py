from package.monitor_cli import cli
from package.resources import network,process,cpu,memory,disk

if __name__ == '__main__':
    args = cli()
    FUNCTION_MAP = {
    'network': network.ipconfig if 'interface' in args and args['interface'] == True else network.netstat,
    'process': process.ps_verbose if 'verbose' in args and args['verbose'] == True else process.ps,
    'cpu': cpu.cpu_info,
    'memory': memory.main,
    'disk': disk.disk_partitions if 'partition' in args and args['partition'] == True else (disk.disk_usage if 'usage' in args and args['usage'] == True else disk.df) 
    }

    f = FUNCTION_MAP.get(args['resource'])
    f()
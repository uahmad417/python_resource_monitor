from package.monitor_cli import cli
from package.resources import network,process,cpu,memory

if __name__ == '__main__':
    args = cli()
    FUNCTION_MAP = {
    'network': network.ipconfig if 'interface' in args and args['interface'] == True else network.netstat,
    'process': process.ps_verbose if 'verbose' in args and args['verbose'] == True else process.ps,
    'cpu': cpu.cpu_info,
    'memory': memory.main
    }
    
    f = FUNCTION_MAP.get(args['resource'])
    f()
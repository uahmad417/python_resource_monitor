import psutil
from datetime import datetime
from package.resources.constants import PS_OUTPUT_FORMAT_VERBOSE, PS_OUTPUT_FORMAT

def ps():
    processes = [proc for proc in psutil.process_iter(['username','pid','name','cpu_percent','memory_percent','cmdline','ppid'])]
    print(PS_OUTPUT_FORMAT.format('PID','NAME','START','COMMAND'))
    for process in processes:
        started = datetime.fromtimestamp(process.create_time()).strftime("%H:%M:%S")
        cmdline = process.info['cmdline'][0] if process.info['cmdline'] else ''
        pid = process.info['pid']
        name = process.info['name']
        print(PS_OUTPUT_FORMAT.format(pid,name,started,cmdline))

#need to work on properly formating cpu_percent and memory_percent
def ps_verbose():
    processes = [proc for proc in psutil.process_iter(['username','pid','name','cpu_percent','memory_percent','cmdline','ppid'])]
    print(PS_OUTPUT_FORMAT_VERBOSE.format('USER','PID','NAME','PPID','%CPU','%MEM','START','COMMAND'))
    for process in processes:
        started = datetime.fromtimestamp(process.create_time()).strftime("%H:%M:%S")
        cmdline = process.info['cmdline'][0] if process.info['cmdline'] else ''
        pid = process.info['pid']
        name = process.info['name']
        user = process.info['username'] if process.info['username'] else ''
        cpu_percent = process.info['cpu_percent']
        memory_percent = process.info['memory_percent']
        ppid = process.info['ppid']
        print(PS_OUTPUT_FORMAT_VERBOSE.format(user,pid,name,ppid,cpu_percent,memory_percent,started,cmdline))

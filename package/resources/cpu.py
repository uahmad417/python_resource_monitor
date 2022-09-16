from platform import platform
import psutil
from package.resources.constants import CPU_OUTPUT_FORMAT

def cpu_info():
    platform = 'Windows' if psutil.WINDOWS else 'Linux'
    cpus = psutil.cpu_count()
    threads = int(psutil.cpu_count()/psutil.cpu_count(logical=False))
    cores = psutil.cpu_count(logical=False)
    cpu_mhz = str(psutil.cpu_freq().max) + ' MHz'
    usage_perc = psutil.cpu_percent()
    cpu_time_user = psutil.cpu_times().user
    cpu_time_system = psutil.cpu_times().system
    cpu_time_idle = psutil.cpu_times().idle
    print(CPU_OUTPUT_FORMAT.format(
        'Platform',platform,
        'CPU(s)',cpus,
        'Thread(s) per core',threads,
        'Core(s) per socket',cores,
        'CPU MHz',cpu_mhz,
        'Usage(%)',usage_perc,
        'CPU Times (user)',cpu_time_user,
        'CPU Times (system)',cpu_time_system,
        'CPU Times (idle)',cpu_time_idle))
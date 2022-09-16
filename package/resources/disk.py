import psutil
from psutil._common import bytes2human
from package.resources.constants import DF_OUTPUT_FORMAT

def disk_partitions():
    for partition in psutil.disk_partitions():
        for name in partition._fields:
            value = getattr(partition,name)
            if name == 'device':
                print('\nDrive: {}\n----------'.format(partition.device))
            else:
                print('{:<15}:{:>15}'.format(name.capitalize(),value))


def disk_usage():
    for partition in psutil.disk_partitions():
        print('\nDrive: {}\n----------'.format(partition.device))
        for name in psutil.disk_usage(partition.device)._fields:
            value = getattr(psutil.disk_usage(partition.device),name)
            print('{:<15}:{:>15}'.format(name.capitalize(),bytes2human(value)))
def df():
    print(DF_OUTPUT_FORMAT.format('Filesystem','Used','Available','Mounted On'))
    for partition in psutil.disk_partitions():
        print(DF_OUTPUT_FORMAT.format(
            partition.fstype,
            bytes2human(psutil.disk_usage(partition.device).used),
            bytes2human(psutil.disk_usage(partition.device).free),
            partition.mountpoint
        ))
from pprint import pprint
import psutil
from psutil._common import bytes2human

def pprint_tuple(nt):
    for name in nt._fields:
        value = getattr(nt,name)
        if name != 'percent':
            value = bytes2human(value)
        print('{:<15}:{:>15}'.format(name.capitalize(),value))
    

def main():
    print('MEMORY\n----------')
    pprint_tuple(psutil.virtual_memory())
    print('\nSwap\n----------')
    pprint_tuple(psutil.swap_memory())

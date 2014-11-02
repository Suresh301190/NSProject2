'''
Created on Nov 2, 2014

@author: Suresh
'''
import hashlib

import psutil
from ids.data.extract import stat


def avg(val, length):
    thresh_hold['cpu_time'] = thresh_hold['cpu_time'] * 1.4 / length
    thresh_hold['thread_count'] = thresh_hold['thread_count'] * 1.4 / length
    thresh_hold['io_0'] = thresh_hold['io_0'] * 1.4 / length
    thresh_hold['io_1'] = thresh_hold['io_1'] * 1.4 / length
    thresh_hold['io_2'] = thresh_hold['io_2'] * 1.4 / length
    thresh_hold['io_3'] = thresh_hold['io_3'] * 1.4 / length
    thresh_hold['mem0'] = thresh_hold['mem0'] * 1.4 / length
    thresh_hold['mem1'] = thresh_hold['mem1'] * 1.4 / length
    thresh_hold['net'] = thresh_hold['net'] * 1.4 / length
    
    return thresh_hold   

def update_max(obj, index, val):
    if(obj[index] < val):
        obj[index] = val      

def err(msg, p):
    return 'High Usage of ' + msg + ' resource by the ' + p.name() + ' process with pid = ' + str(p.pid)

def tos(val):
    s = ''
    for i in val:
        s += ',' + i[0]
    return hashlib.sha1(s[1:]).hexdigest()

if __name__ == '__main__':
    thresh_hold = dict(cpu_time = 0.0, 
                       thread_count = 0, 
                       io_0 = 0,
                       io_1 = 0,
                       io_2 = 0,
                       io_3 = 0,
                       mem0 = 0,
                       mem1 = 0,
                       net = 0,
                       hash = set())
    
    for line in list(open('../Sample1.txt', 'r')):
        parts =  line[:-1].split(',')
        thresh_hold['cpu_time'] += float(parts[0])
        thresh_hold['thread_count'] += long(parts[1])
        thresh_hold['io_0'] += long(parts[2])
        thresh_hold['io_1'] += long(parts[3])
        thresh_hold['io_2'] += long(parts[4])
        thresh_hold['io_3'] += long(parts[5])
        thresh_hold['mem0'] += long(parts[6])
        thresh_hold['mem1'] += long(parts[7])
        thresh_hold['net'] += long(parts[8])
        thresh_hold['hash'].update([parts[9]])
        
    print thresh_hold
    avg(thresh_hold, 300.0)
    
    print thresh_hold
    
    p = psutil.Process(7768)
    for i in range(10):
        parts = stat(p, .3).split(',')
        print parts
        if(long(parts[0]) > thresh_hold['cpu_time']):
            print err('CPU', p)
        if(long(parts[1]) > thresh_hold['thread_count']):
            print err('thread class', p)
        if(long(parts[2]) > thresh_hold['io_0']):
            print err('Disk IO', p)
        if(long(parts[3]) > thresh_hold['io_1']):
            print err('Disk IO', p)
        if(long(parts[4]) > thresh_hold['io_2']):
            print err('Disk IO', p)
        if(long(parts[5]) > thresh_hold['io_3']):
            print err('Disk IO', p)
        if(long(parts[6]) > thresh_hold['mem0']):
            print err('Memory', p)
        if(long(parts[7]) > thresh_hold['mem1']):
            print err('Memory', p)
        if(long(parts[8]) > thresh_hold['io_0']):
            print err('Network IO', p)
        if(tos(p.open_files()) not in thresh_hold['hash']):
            print 'Accessing files which it should not use'
        
        
        
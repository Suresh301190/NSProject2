'''
Created on Oct 25, 2014

@author: Suresh
'''

import psutil
import hashlib

def gs(val):
    if(val == 0):
        return '0'
    return format(val)

def tos(val):
    s = ''
    for i in val:
        s += ',' + i[0]
    return s[1:]

def gh(val):
    return hashlib.sha1(val).hexdigest()

def normalize():
    lines = list(open('D:\Luna_Workspace\IntrusionDetectionSystem\Output.txt', 'r'))
    print lines
    return

def stat(p, interval = 5.0):
    cpu = gs(p.cpu_percent(interval))
    io = p.io_counters()
    mem = p.memory_info()
    toprint = (cpu + ','
               + gs(p.num_threads()) + ','
               + gs(io[0]) + ','
               + gs(io[1]) + ','
               + gs(io[2]) + ',' 
               + gs(io[3]) + ','
               + gs(mem[0]) + ','
               + gs(mem[1]) + ','
               + gs(len(p.connections('all'))) + ','
               + gh(tos(p.open_files()))
               )
    return toprint

if __name__ == '__main__':
    msg = hashlib.sha1()
    p = psutil.Process(7768)
    print p.create_time()
    print p.io_counters()
    print p.memory_info()
    print tos(p.open_files())
    print gh(tos(p.open_files()))
    
    for i in range(2):
        print stat(p, 5.0)
        
    normalize()
        
#!/usr/bin/env python
from multiprocessing import Process
import os

def run_proc(name):
    print 'Run child process %s (%s) ...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    p1 = Process(target=run_proc, args=('test1',))
    print 'Process will start.'
    p.start()
    p.join()
    
    p1.start()
    p1.join()
    print 'Porcess end.'

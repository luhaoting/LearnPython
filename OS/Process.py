#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os,time 

def __Is_Process_Running(imagename):
    p = os.popen('tasklist /FI "IMAGENAME eq %s"' % imagename)
    return p.read().count(imagename)

def CycCheckProc():
    while True:
        time.sleep(10)
        pid = __Is_Process_Running('Server.exe')
        if pid <= 0:
            # code .... 重启server.exe进程
            break

if __name__ == "__main__":
    CycCheckProc()
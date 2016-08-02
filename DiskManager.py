import shutil
import itertools
import ctypes
import os
import string
import platform
import psutil



def Space():
     try:
         print(shutil.disk_usage("/"))
     except Exception():
         print(Exception)
def Partitions():
    try:
        print(psutil.disk_partitions())
    except Exception():
        print(Exception)
def CPU_Stats():
    try:
        print(psutil.cpu_stats())
    except Exception():
        print(Exception)
def CPU_Percent():
    try:
        print(psutil.cpu_percent())
    except Exception():
        print(Exception)
def DiskCounters():
    try:
        print(psutil.disk_io_counters())
    except Exception():
        print(Exception)
def Users():
    try:
       print(psutil.users())
    except Exception():
        print(Exception)










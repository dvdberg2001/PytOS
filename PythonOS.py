import os
from time import ctime
import subprocess
import platform
from time import sleep
from collections import namedtuple





### FUNCTIONS ###

def Start_os():
    print("+++++++++++++++++++++++++")
    print("+    Welcome on PytOS   +")
    print("+       Version 0.8.6   +")
    print("+       Try helpme()    +")
    print("+     Still in BETA     +")
    print("+++++++++++++++++++++++++")

def display_title_bar():
    print("")
    

def helpme():
    print("----------------------------------------------")
    print("|                    HELP:                   |")
    print("|         CWT = Clear Windows terminal       |")
    print("|         CLT = Clear Linux terminal         |")
    print("|         ProCommand = Working on it         |")
    print("|         tictactoe = A funny game           |")
    print("|         DiskSpace = Show the diskspace     |")
    print("|         Time_Now = The time right now      |")
    print("|        About_me = let us now we you are    |")
    print("|        More_info = Many info of the OS     |")
    print("|        My_info = Info about myself         |")
    print("|        shutdown =  Shut system down        |")
    print("|   lin_update = Only for Linux","updating OS  |")
    print("|    Notepad = Open in windows Notepad       |")
    print("|    device_specs = Show device specs        |")
    print("----------------------------------------------")
    
    


def CWT():
    os.system("cls")



def CLT():
    os.system("clear")


def Time_Now():
    print(ctime())


def About_me():
    print("Say somthing about you")
    name = input("What is your name: ")
    age = input("What is your age: ")
    birthday = input("What is your birthday: ")







    


def shutdown():
    os.system("sudo shutdown -h now")
    subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
    print("Shutting down in 60 sec. type {SDown} to cancel")
    

    
    


def lin_update():
    os.system("sudo apt-get update")
    print(os.system)


def device_spec():
    print(platform.machine())
    print(platform.version())
    print(platform.platform())
    print(platform.uname())
    print(platform.system())
    print(platform.processor())


def restart():
    os.system("shutdown /r")
    os.system("sudo reboot")
    print("Restarting. type {SDown} to cancel")
    


    

def SShutdown():
    os.system("shutdown /a ")


def More_info():
    print("----------------------------------")
    print("|   Current Version is 0.7.4     |")
    print("|        PYTHON BASED OS         |")
    print("|       CROSS-PLATFORM OS        |")
    print("| {DEVELOPT IN THE NETHERLANDS}  |")
    print("|         <MADE BY:/>            |")
    print("|    <{DAAN VAN DEN BERG}/>      |")
    print("----------------------------------")

def notepad():
    print("Notepad opening...")
    sleep(0.95)
    print("Notepad Launched")
    subprocess.call(["notepad"])
    print("Notepad closed")

   
 
   
  
     



    

    
    

### MAIN PROGRAM ###


Start_os()
from SecurityLib import *
choice = ''

display_title_bar()
while choice != 'quit':    
    
    
    
    choice = input("<PytOS@Computer> ")
    
    
    display_title_bar()
    if choice == 'helpme':
       helpme()
    elif choice == 'CWT':
        CWT()
    elif choice == 'CLT':
        CLT()
    elif  choice == 'Time_Now':
        Time_Now()
    elif choice == 'About_me':
        About_me()
    elif choice == 'shutdown':
        shutdown()
    elif choice == '{SDown}':
        SShutdown()
    elif choice == 'device_specs':
        device_spec()
    elif choice == 'restart':
        restart()
    elif choice == 'More_info':
        More_info()
    elif choice == 'quit':
        print("Shutting down the system.")
    elif choice == 'Notepad':
        notepad()    
    elif choice == 'ProCommand':
       from ProCommandLib import ProCommand
    elif choice == 'test':
         from RaspberryPiLib import GPIO_Control
    elif choice == 'tictactoe':
        from TicTacToe import *
    elif choice == 'DiskSpace':
        from DiskManager import FreeDiskSpace
    elif choice == 'Procceslist':
        from ProcessesLib import ProccesInfo
    elif choice == 'UserInfo':
        from ProccesLib import UserInformation
    elif choice == '': 
        print("That is wrong. Try to typ somthing.")
    else:
        print(choice,"is a wrong command. Try again. (helpme)")

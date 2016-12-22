### CBP(Command Based Programming)
### Version 0.0.1
### For PytOS
import subprocess
import os
from time import sleep



def ProccesInfo():
   Enter = ''
   Enter = input('press enter')
   while Enter == '':
      subprocess.call("tasklist")
      sleep(30)
      os.system("cls")
      if Enter == 'exit':
         break
      from PythonOS import PytOS
def UserInformation():
   os.system("echo %username%")
def Computer_Tree():
    os.system("tree")



Computer_Tree()
UserInformation()
ProccesInfo()

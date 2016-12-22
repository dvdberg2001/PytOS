import os
from time import ctime
import subprocess
import platform
from time import sleep
from collections import namedtuple


### BEGIN
ProCommand = ''

Enter = input("Press enter")

def BeforeCommand ():
     print("/^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\"")
     print("{          Welcome on ProCommand           }")
     print("{     Program from the PytOS Command line  }")
     print("{          Starting The Program            }")
     print("{                almost ready              }")
     print("\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~/")
     print("")
     print("Please add even the sort of document like .txt .sh")
     Docname = input("Document name: ")
     Docname
     print("{DEVELOPING",Docname,"}")

     
      

if Enter == '':
             print("Starting")
             sleep(1)
             print("") 
    
BeforeCommand()
    

while ProCommand != 'save':
      input("") 
      if ProCommand == "save":
          os.mkdir(Docname)
          print("ENDED PROCOMMAND")
          break

import PythonOS

       


 
    

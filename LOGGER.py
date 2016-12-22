### Log Writer

""""
try:
  Text = open("write.txt", "w")
  txt = input("What is the text")
  Text.write(txt)
  Text.close()
  print("Saved the text")
except Exception:
    print(Exception)

Text = open("write.txt", "r")
print(Text.read())
Text.close()
"""

### SECURITY LIBARY FOR COMMANDLINE###
from time import sleep
import  os.path



import os
import os.path

PATH='./USER.txt'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    try:
     USER = open("USER.txt", "r")
     USERTxT = open("USER.txt", "r")
     USER.close()
     LOG = ''
     while LOG != USERTxT():
         LOG = input("Username:")
         if LOG == USERTxT():
             from PythonOS import *

    except NameError():
        print(NameError)

else:
    try:
      USER = open("USER.txt", "w")
      USERNAME = input("What is your name: ")
      USER.write(USERNAME)
      USER.close()
      print(USER, "Your profiel is maked.")
    except NameError():
      print(NameError)




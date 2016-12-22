### Internet libary for windows

import subprocess as sp
import urllib


    
def ipcheck():
  status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
  if status == 0:
      print("System " + str(pop) + " is UP !")
  else:
      print("System " + str(pop) + " is DOWN !")


pop = input("Enter the ip address: ")
ipcheck()

def Connection():
  import socket
  ipaddress=socket.gethostbyname(socket.gethostname())
  if ipaddress=="127.0.0.1":
      print("You are not connected to the internet!")
  else:
      print("You are connected to the internet with the IP address of "+ ipaddress )
         
  
    

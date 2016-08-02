### SECURITY LIBARY FOR COMMANDLINE###
from time import sleep

def Make_USER():
    try:
        USER = open("USER.txt", "w")
        USERNAME = input("What is your name: ")
        USER.write(USERNAME)
        USER.close()
        print(USER, "Your profiel is maked.")
    except Exception():
        print(Exception)




username = ''
password = ''

while username != 'PytOS':
      username = input("Username: ")


         print("Loading...")
         sleep(0.25)
         print("---------------")
      else:
         print("Loading...")
         sleep(0.75)
         print("Wrong Username")

while password != 'Computer':
      password = input("Password: ")

      if password == 'Computer':
         print("Loading...")
         sleep(0.25)
         print("Login Completed")
      else:
         print("Loading...")
         sleep(0.25)
         print("Login Failed")








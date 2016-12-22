### PasswordCreator

def Make_USER():
    try:
        Look = open("USER.txt", "r")
        USER = open("USER.txt", "w")
        USERNAME = input("What is your name: ")
        USER.write(USERNAME)
        USER.close()
        print(USER, "Your profiel is maked.")
    except Exception():
        print(Exception)
Make_USER()

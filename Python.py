
import time
registered_username = None
Login_password = None

print("\__||-__-||__/ - This Tool Made By Wctos")

def Register():
    while True:
        Username = input(' > Enter Your Username: ')
        Password = input(' > Enter Your Password: ')
        Confirm = input(' > Confirm Password: ')
        if Confirm == Password:
            global registered_username
            global Login_password
            print(" > Done")
            break
        else:
            print(" > Error, Password Does not match!")
            continue

def Login():
    global registered_username
    global Login_password
    while True:
        Usern = input(' > Enter Your Username: ')
        if Usern == registered_username:
            print(" > Correct")
        else:
            print(" > no username listed")
            break

        Passwd = input(' > Enter Your Password: ')
        if Passwd == Login_password:
            print(" > Correct!")
        else:
            print(" > no password listed! ")
            break

print(" > Enter 'Register' to register")
print(" > Enter 'Login' to login")

reg_login = input('Do you want to register or login? : ')
if reg_login == 'Register':
    Register()

elif reg_login == 'Login':
    Login()

else:
    print("Error, wrong input")

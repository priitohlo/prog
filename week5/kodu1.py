import re

password_ok = False

def check_password(pw1, pw2):
    if (pw1 == pw2) and re.match('(?=.*?[0-9])(?=.*?[A-Za-z]).{8,}', pw1):
        return True
    else:
        return False

username = input("Sisesta kasutajanimi: ")

while (not password_ok):
    in_pw1 = input("Sisesta parool: ")
    in_pw2 = input("Sisesta parool uuesti: ")

    if check_password(in_pw1, in_pw2):
        password_ok = True
        password = in_pw1[::-1]

with open('users.txt', 'a') as f:
    f.write(username + ':' + password)
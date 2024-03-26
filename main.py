from cryptography.fernet import Fernet

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
"""


def load_key():
    return open("key.key", "rb").read()


key = load_key()

master_password = input("Enter your master password: ")


def add():
    name = input("What is the name of the account? ")
    password = input("What is the password? ")

    with open("passwords.txt", "a") as f:
        f.write(name + " | " + password + "\n")


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(" | ")
            print("user: " + user + ", password: " + password)


while True:
    mode = input(
        "would you like to add a new password or view an existing one (view/add/ q), press q to quit: ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid option")
        continue

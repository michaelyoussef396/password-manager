master_password = input("Enter your master password: ")

mode = input(
    "would you like to add a new password or view an existing one (view/add): ").lower()

if mode == "view":
    pass
elif mode == "add":
    pass
else:
    print("Invalid option")

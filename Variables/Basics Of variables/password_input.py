# import getpass so the password is not displayed
from getpass import getpass

username = input("Enter username:")

# ask for password securely
# unlike input(), getpass() hides password
password = getpass("Enter password:")
print("Username:", username)
print("Password received successfully.")
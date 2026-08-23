password = "Muskan123!" # string variable

length = len(password)
has_digit = any(char.isdigit() for char in password) # check if digits exists
has_special = any(char in "!@#$%^&*" for char in password) # checks if any special char exists

if length >= 8 and has_digit and has_special:
    print("Strong Password!")
elif length >= 6 and has_digit:
    print("Medium Password!")
else:
    print("Weak Password!")
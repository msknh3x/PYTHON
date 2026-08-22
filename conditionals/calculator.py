a = 10
b = 5
operation = "add"

if operation == "add":
    print("Result:", a + b)
elif operation == "subtract": # runs only when the first condition was false
    print("Result:", a - b)
else:
    print("Invalid Operation")
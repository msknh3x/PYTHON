def calculator(a,b, operation):
    if operation == "add":
        return a + b
    elif operation == "Subtract":
        return a - b
    else:
        return "Invalid Operation"

print("Add:", calculator(10,5, "add"))
print("Subtract:", calculator(10,5, "Subtract"))
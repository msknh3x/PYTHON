# Prime Numbers Finder

limit = int(input("Enter limit: "))

print("Prime numbers up to", limit, ":")
for num in range(2, limit + 1):   # loop from 2 to limit
    is_prime = True
    for i in range(2, num):       # check divisibility
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

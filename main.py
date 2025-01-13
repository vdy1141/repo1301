def factorial(num):
    if num < 0:
        print("Can't calculate factorial")
        return
    if num <= 1:
        print("Factorial is ", 1)
        return
    fact = 1
    for i in range(2, num+1):
        fact = fact * i
    print("The factorial is", fact)
    return

factorial(5)

def primeNumber(n):
    if n< 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % 1== 0:
            return False
    return True
def fizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif primeNumber(i):
            print("Prime")
        else:
            print(i)
fizzBuzz()

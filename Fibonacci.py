def Fibonacci(x):
    if x == 0 or x == 1:
        return x
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)

print(Fibonacci(2))
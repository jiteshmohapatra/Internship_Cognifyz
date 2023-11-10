#Write a Python function that generates theFibonacci sequence up to a given number ofterms. The function should take an integerinput from the user and display theFibonacci sequence up to that number ofterms.

def fibonacci(n):
    fib_sequence = [0,1]
    while len(fib_sequence)<n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence
n = int(input("enter a fibonacci term you want"))
result = fibonacci(n)
print(f"The {n}-th Fibonacci term is {result}")
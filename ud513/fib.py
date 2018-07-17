"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    a = 0
    b = 1
    return fib(a, b, position)
    

def fib(a, b, position):
    if position == 0:
        return a
    else:
        return fib(b, a+b, position-1)

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)

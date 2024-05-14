# CodeAlpha
Task1:FIBONACCI SERIES
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    return fib_series[:n]

# Example usage
n = 10
fib_series = fibonacci(n)
print(fib_series)
This Python code defines a function fibonacci(n) to generate the Fibonacci series up to the nth term using iteration. Here's an explanation of the code:

Function Definition: The fibonacci(n) function takes an integer n as input, representing the number of terms in the Fibonacci series to generate.

Initialization: Inside the function, a list fib_series is initialized with the first two Fibonacci numbers, [0, 1].

Loop for Generating Fibonacci Series: The code enters a for loop starting from 2 up to n-1. This loop iteratively calculates the next Fibonacci number by adding the last two numbers in the fib_series list.

Calculating Next Fibonacci Number: In each iteration of the loop, the next Fibonacci number (next_fib) iscalculated as the sum of the last two numbers in fib_series (fib_series[-1] and fib_series[-2]).

Appending Next Fibonacci Number: The calculated next_fib is then appended to the fib_series list using fib_series.append(next_fib).

Return and Truncation: Finally, the function returns a truncated version of the fib_series list containing only the first n Fibonacci numbers using slicing (fib_series[:n]).

Example Usage: In the example provided, n = 10, so the function generates the first 10 Fibonacci numbers and stores them in fib_series, which is then printed.

This code is efficient for generating Fibonacci numbers iteratively, especially for large values of n, as it doesn't involve the overhead of function calls and stack operations like recursive approaches.

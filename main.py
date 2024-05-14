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
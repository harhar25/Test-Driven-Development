def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed")
    if n == 0:
        return 1
    return n * factorial(n - 1)
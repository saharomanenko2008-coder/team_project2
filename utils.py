def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
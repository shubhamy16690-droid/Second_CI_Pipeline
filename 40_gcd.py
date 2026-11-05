def gcd(a, b):
    """Return the greatest common divisor using the Euclidean algorithm."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(gcd(x, y))

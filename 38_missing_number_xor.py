def find_missing_number(numbers, n):
    """
    numbers contains n-1 distinct values from 1..n (one is missing).
    Return the missing number using XOR.
    """
    result = 0
    for i in range(1, n + 1):
        result ^= i
    for x in numbers:
        result ^= x
    return result


if __name__ == "__main__":
    n = int(input("Enter n: "))
    data = list(map(int, input("Enter the n-1 numbers: ").split()))
    print(find_missing_number(data, n))

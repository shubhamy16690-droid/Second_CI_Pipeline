def is_sorted(items):
    """Return True if the list is sorted in ascending order."""
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


if __name__ == "__main__":
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    print(is_sorted(data))

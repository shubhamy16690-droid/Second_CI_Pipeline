def move_zeros(items):
    """Move all zeros to the end, keeping the order of other elements."""
    non_zeros = [x for x in items if x != 0]
    zeros = [0] * (len(items) - len(non_zeros))
    return non_zeros + zeros


if __name__ == "__main__":
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    print(move_zeros(data))

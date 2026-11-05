def most_frequent(items):
    """Return the most frequent element (first one wins on a tie), or None."""
    if not items:
        return None
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    best = items[0]
    for x in items:
        if counts[x] > counts[best]:
            best = x
    return best


if __name__ == "__main__":
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    print(most_frequent(data))

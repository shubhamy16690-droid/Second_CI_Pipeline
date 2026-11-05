def first_non_repeating(text):
    """Return the first character that appears only once, or None."""
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in text:
        if counts[ch] == 1:
            return ch
    return None


if __name__ == "__main__":
    s = input("Enter a string: ")
    print(first_non_repeating(s))

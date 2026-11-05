def rotate_string(text, k):
    """Rotate the string to the left by k positions."""
    if not text:
        return text
    k = k % len(text)
    return text[k:] + text[:k]


if __name__ == "__main__":
    s = input("Enter a string: ")
    k = int(input("Enter K: "))
    print(rotate_string(s, k))

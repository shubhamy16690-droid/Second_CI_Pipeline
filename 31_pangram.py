def is_pangram(sentence):
    """Return True if the sentence contains every letter a-z at least once."""
    letters = {ch for ch in sentence.lower() if ch.isalpha()}
    return len(letters) == 26 and all("a" <= ch <= "z" for ch in letters)


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(is_pangram(text))

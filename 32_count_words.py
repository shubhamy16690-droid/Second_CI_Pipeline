def count_words(sentence):
    """Return the number of words in a sentence."""
    return len(sentence.split())


if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print(count_words(text))

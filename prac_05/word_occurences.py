"""
Word Occurrences
Estimate:  40 minutes
Actual:
"""


def main():
    """Count the occurrences of words in a string."""
    string = "this is a collection of words of nice words this is a fun thing it is"  # input("Text: ")

    words = string.split()
    unique_words = set(words)
    word_to_lengths = {}
    for word in unique_words:
        word_to_lengths[word] = words.count(word)
        print(f"{word} : {word_to_lengths[word]}")


main()

"""
Word Occurrences
Estimate:  40 minutes
Actual:    13 minutes
"""


def main():
    """Count the occurrences of words in a string."""
    string = input("Text: ")

    # Count word occurrences.
    words = string.split()
    unique_words = set(words)
    word_to_lengths = {}
    for word in unique_words:
        word_to_lengths[word] = words.count(word)

    # Display sorted.
    max_length = max(len(word) for word in unique_words)
    for word in sorted(word_to_lengths.keys()):
        print(f"{word:{max_length}} : {word_to_lengths[word]}")


main()

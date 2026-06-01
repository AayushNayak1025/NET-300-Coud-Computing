# This code calculates the frequency of words in a given text and prints the top 3 most common words along with their counts.

text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""

def word_frequency(text):
    text = text.lower()

    for mark in ".,!?;:\"'":
        text = text.replace(mark, "")

    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    top_words = sorted(
        freq.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    return top_words

print("\nTop 3 Words:")
for word, count in word_frequency(text):
    print(f"{word} — {count} times")
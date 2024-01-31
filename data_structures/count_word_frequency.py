def count_word_frequencies(corpus):
    word_freq = {}  # Multidimensional dictionary to store word frequencies

    for document in corpus:
        words = document.split()

        for word in words:
            if word not in word_freq:
                word_freq[word] = {'total_count': 1, 'documents': {document: 1}}
            else:
                word_freq[word]['total_count'] += 1
                if document in word_freq[word]['documents']:
                    word_freq[word]['documents'][document] += 1
                else:
                    word_freq[word]['documents'][document] = 1
    return word_freq

corpus = [
    "This is the multidimensional dictionary.",
    "This dictionary stores the sub dictionary.",
    "And this is the third containing the word and count.",
    "Is this the first level of dictionary?"
]

word_frequencies = count_word_frequencies(corpus)

# Displaying word frequencies
for word, info in word_frequencies.items():
    print(f"Word: {word}")
    print(f"  Total Count: {info['total_count']}")
    print("  Document Occurrences:")
    for document, count in info['documents'].items():
        print(f"    {document}: {count}")
    print()
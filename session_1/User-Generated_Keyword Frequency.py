from collections import Counter
import re


def analyze_text_data(text_data):
    combine_text=" ".join(text_data)

    combine_text=combine_text.lower()

    words=re.findall(r'\b\w+\b',combine_text)

    print(words)

    key_words_counts=Counter(words)

    for key,value in key_words_counts.items():
        print(f"{key}-{value}")



text_data = [
    "User-generated text data for keyword frequency analysis.",
    "Analyzing text data helps to understand user preferences.",
    "This is an example of analyzing keyword frequency in Python."
]

analyze_text_data(text_data)
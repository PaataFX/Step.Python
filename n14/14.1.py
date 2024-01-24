from collections import Counter
import re

def second_most_frequent_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_text = re.sub(r'[^\w\s]', '', content).lower()

    words = cleaned_text.split()

    word_counts = Counter(words)

    most_common_words = word_counts.most_common(2)
    
    if len(most_common_words) >= 2:
        second_most_common_word, second_count = most_common_words[1]
        print(f"The second most frequently repeated word is '{second_most_common_word}' with {second_count} occurrences.")
    else:
        print("Not enough words in the document to determine the second most frequent word.")

if __name__ == "__main__":
    file_path = "article.txt"
    second_most_frequent_word(file_path)

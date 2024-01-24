# article.tx ფაილში პოულობს რიგით მეორე ყვეალზე მეტად განმეორებულ სიტყვას
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

# გადმოაქვს names cvs ტიპიდან txt ფაილში (თუ ერთი ქოლამნია სახელების და არა ორი ლისთი.)

import csv

def copy_csv_to_txt(csv_file, txt_file):
    try:
        with open(csv_file, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            names = [row[0] for row in reader]

        with open(txt_file, 'w', encoding='utf-8') as txt_file:
            for name in names:
                txt_file.write(name + '\n')

        print(f"Successfully copied information from '{csv_file}' to '{txt_file}'.")
    except FileNotFoundError:
        print(f"Error: '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    csv_file_path = "names.csv"
    txt_file_path = "names.txt"

    copy_csv_to_txt(csv_file_path, txt_file_path)


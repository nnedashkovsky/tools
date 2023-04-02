from collections import defaultdict
import os

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def clean_text(text, lowercase=True):
    for char in ['.', ',', '!', '?', ':', ';', '—', '«', '»', '(', ')', '[', ']', '{', '}']:
        text = text.replace(char, '')
    if lowercase:
        text = text.lower()
    return text

def generate_ngrams(text, n):
    ngrams = defaultdict(int)
    for i in range(len(text) - n + 1):
        if all(text[i + j].isalpha() for j in range(n)):
            ngrams[text[i:i + n]] += 1
    return ngrams

def save_ngrams_to_file(ngrams, file_name):
    results_folder = '_results'
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    ngrams_sorted = sorted(ngrams.items(), key=lambda x: x[1], reverse=True)
    with open(os.path.join(results_folder, file_name), 'w', encoding='utf-8') as f:
        for ngram in ngrams_sorted:
            f.write(ngram[0] + ' ' + str(ngram[1]) + '\n')

def count_the_combination(max_letters, file_path, lowercase=True):
    text = read_text(file_path)
    cleaned_text = clean_text(text, lowercase=lowercase)
    file_name_prefix = os.path.splitext(os.path.basename(file_path))[0]
    register_suffix = "lower" if lowercase else "original"

    for n in range(2, max_letters+1):
        ngrams = generate_ngrams(cleaned_text, n)
        save_ngrams_to_file(ngrams, f'{file_name_prefix}_russian_{n}grams_{register_suffix}.txt')

if __name__ == '__main__':
    file_path = input("Enter the file path: ")
    max_letters = int(input("Enter the maximum number of letters in combination: "))

    count_the_combination(max_letters, file_path, lowercase=True)
    count_the_combination(max_letters, file_path, lowercase=False)

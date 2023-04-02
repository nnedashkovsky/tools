# count letters combination

This script counts n-grams of a given text file and saves the results in a folder named `_results`. It allows you to specify the maximum number of letters in a combination.

## Usage

1. Make sure you have Python 3.x installed on your system.

2. Place the script (`count_letters_combination.py`) and the text file you want to analyze in the same directory.

3. Open a terminal or command prompt, navigate to the directory containing the script and the text file, and run the following command:

count_letters_combination

4. You will be prompted to enter the file path and the maximum number of letters in a combination. Enter the required information and press Enter.

5. The script will process the text file, generating n-grams, and save the results in the `_results` folder.

## Script Functions

- `read_text(file_path)`: Reads the content of a text file.
- `clean_text(text, lowercase=True)`: Cleans the text by removing punctuation and optionally converting it to lowercase.
- `generate_ngrams(text, n)`: Generates n-grams from the cleaned text.
- `save_ngrams_to_file(ngrams, file_name)`: Saves the n-grams and their counts to a file in the `_results` folder.
- `count_the_combination(max_letters, file_path, lowercase=True)`: Main function that combines the above functions to count n-grams and save the results.

## License

This script is released under the MIT License.


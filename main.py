import sys
from stats import get_num_words, get_times_characters, get_sorted_characters

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()
  
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    word_count = get_num_words(book_text)
    times_characters = get_times_characters(book_text)
    sorted_characters = get_sorted_characters(times_characters)
    print(f"Found {word_count} total words")
    sorted_characters
    for item in sorted_characters:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


main()
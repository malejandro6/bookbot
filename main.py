from stats import word_count
from stats import character_count
from stats import sort_characters
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text (book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count_result = word_count(book_text)
    char_counts = character_count(book_text)
    sorted_chars = sort_characters(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()

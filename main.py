def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

import sys

from stats import count_words, count_chars, chars_dict_to_sorted_list

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_chars(text)
    sorted_chars = chars_dict_to_sorted_list(num_chars)
    # print(f"{num_words} words found in the document")
    # print(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue 
        print(f"{item["char"]}: {item["num"]}")   
    print("============= END ===============")     
main()
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words, count_characters

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    num_characters = count_characters(text)
    result_message = f"{num_words} words found in the document"
    print(result_message)
    print(num_characters)
main()
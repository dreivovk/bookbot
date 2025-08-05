def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    return len(text.split())

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    result_message = f"{num_words} words found in the document"
    print(result_message)
main()
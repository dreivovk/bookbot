def count_words(text):
    return len(text.split())

def count_characters(text):
    char_dictionary = {}
    for character in text:
        low_char = character.lower()
        if low_char in char_dictionary:
            char_dictionary[low_char] += 1
        else:
            char_dictionary[low_char] = 1
    return char_dictionary
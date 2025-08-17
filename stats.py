def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dictionary = {}
    for character in text:
        low_char = character.lower()
        if low_char in char_dictionary:
            char_dictionary[low_char] += 1
        else:
            char_dictionary[low_char] = 1
    return char_dictionary

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(char_dictionary):
    dict_list = []
    for char in char_dictionary:
        number = char_dictionary[char]
        dict_list.append({"char": char, "num": number})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

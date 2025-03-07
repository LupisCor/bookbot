def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def dict_to_list(char_dict):
    char_lst = []
    for char in char_dict:
        count = char_dict[char]
        if char.isalpha():
            char_lst.append({"char": char, "num": count})
    return char_lst
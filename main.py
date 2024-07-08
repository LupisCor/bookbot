def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_characters(text)
    char_list = dict_to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for i in range(0, len(char_list)):
        print(f"The '{char_list[i]['char']}' character was found {char_list[i]['num']} times")
    print("--- End report ---")


def sort_on(dict):
    return dict["num"]

def dict_to_list(char_dict):
    char_list = []
    for char in char_dict:
        count = char_dict[char]
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    return(char_list)


def get_num_characters(text):
    char_dict = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
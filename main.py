def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(char_dict)


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
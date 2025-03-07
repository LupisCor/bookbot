from stats import get_num_words, get_num_characters, dict_to_list, sort_on
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    char_dict = get_num_characters(text)
    char_list = dict_to_list(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    # print(f"--- Begin report of {book_path} ---")
    print(f"Found {num_words} total words\n")
    for i in range(0, len(char_list)):
        print(f"{char_list[i]['char']}: {char_list[i]['num']}")
        # print(f"The '{char_list[i]['char']}' character was found {char_list[i]['num']} times")
    # print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
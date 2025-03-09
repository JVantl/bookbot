import sys
from stats import characters, word_count, chars_dict_to_sorted_list
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_books>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_of_words = word_count(text)
    chars_dict = characters(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_of_words, chars_sorted_list)
def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_of_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}'")
    print("============= END ===============")


main()

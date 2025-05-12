import sys
from stats import get_num_words, sort_letters_dict


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    content = get_book_text(book)
    num_words = get_num_words(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    s = sort_letters_dict(content)
    for k in s:
        c = k["char"]
        if c.isalpha():
            print(f"{k["char"]}: {k["num"]}")
        else:
            continue
    print("============= END ===============")


main()

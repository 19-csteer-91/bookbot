import sys
from stats import get_num_words, get_counts, chars_to_list

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    counts = get_counts(text)

    sorted_chars = chars_to_list(counts)

    for item in sorted_chars:
        char=item["char"]
        num = item["num"]

        if not char.isalpha():
            continue

        print(f"{char}: {num}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()
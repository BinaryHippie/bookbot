import sys
from stats import count_words, count_chars, sort_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    book_text = get_book_text(path_to_file)

    # Count words
    num_words = count_words(book_text)

    # Count characters & sort
    char_counts = count_chars(book_text)
    sorted_chars = sort_count(char_counts)

    # Print report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")
    
main()

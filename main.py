from stats import count_words, count_letters, generate_report
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents=file.read()
    return file_contents



def main():
    if len(sys.argv) == 2:
        book_name = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_data = get_book_text(book_name)
    num_words = count_words(book_data)
    num_letters = count_letters(book_data)
    generate_report(book_name,num_words,num_letters)

main()

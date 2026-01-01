from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents=file.read()
    return file_contents



def main():
    book_name = "books/frankenstein.txt"
    book_data = get_book_text(book_name)
    num_words = count_words(book_data)
    print(f"Found {num_words} total words")
    num_letters = count_letters(book_data)
    print(num_letters)

main()

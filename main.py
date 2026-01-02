from stats import count_words, count_letters, generate_report

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents=file.read()
    return file_contents



def main():
    book_name = "books/frankenstein.txt"
    book_data = get_book_text(book_name)
    num_words = count_words(book_data)
    num_letters = count_letters(book_data)
    generate_report(book_name,num_words,num_letters)

main()

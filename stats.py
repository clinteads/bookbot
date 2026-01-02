def count_words(text):
    return len(text.split())

def count_letters(text):
    result = {}
    for c in text.lower():
        if c not in result:
            result[c] = 0
        result[c] += 1
    return result

def sort_on(items):
    return items[e]

def convert_letter_count_dict(letter_count):
    result = []
    sorted_dict = dict(sorted(letter_count.items(), key=lambda item: item[1],reverse=True))
    for key in sorted_dict:
        if key.isalpha():
            result.append({key:letter_count[key]})
    return result
    

def generate_report(filename, word_count, letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    result = convert_letter_count_dict(letter_count)
    for item in result:
        for k,v in item.items():
            print(f"{k}: {v}")
    print("============ END ===============")

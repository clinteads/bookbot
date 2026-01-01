def count_words(text):
    return len(text.split())

def count_letters(text):
    result = {}
    for c in text.lower():
        if c not in result:
            result[c] = 0
        result[c] += 1
    return result
def main():
    book_path = "./books/frankenstein.txt"
    text = read_book(book_path)
    words = count_words(text)
    letters = count_letters(text)
    print(letters)

def read_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    non_duplicate_letters = text.lower()
    letters_dict = {}
    for letter in non_duplicate_letters:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

main()

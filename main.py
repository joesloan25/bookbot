def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(book_text)} words found in this document. \n")

    character_counts = get_character_counts(book_text)
    sorted_counts = sorted(character_counts.items(), key = lambda x:x[1], reverse = True)
    for character,count in sorted_counts:
        print(f"The '{character}' character was found {count} times")

    print("--- End Report ---")


def get_book_text(book_path):
    with open(book_path) as f:
         return f.read()


def get_word_count(book_text):
    words = book_text.split()
    return(len(words))

def get_character_counts(book_text):
    lowered_text = book_text.lower()
    character_counts = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        character_counts[char] = 0

    for character in lowered_text:
        if character in alphabet:
            character_counts[character] += 1
        else:
            continue

    return character_counts

main()

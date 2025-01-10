def main():
    book_to_read = "books/frankenstein.txt"
    book_text = get_book_text(book_to_read)
    word_count = get_word_count(book_text)
    character_counts = get_character_counts(book_text)
    print_report(book_to_read, word_count, character_counts)

def get_book_text(book):
    with open(book) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    character_counts = {}
    for char in text:
        if char.isalpha() == False:
            continue
        char = char.lower()
        if char not in character_counts:
            character_counts[char] = 0
        character_counts[char] += 1
    return character_counts

def print_report(book, word_count, character_counts):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document.\n")

    for char, count in character_counts.items():
        print(f"The '{char}' character was found {count} times.")

    print("--- End report ---")

if __name__ == "__main__":
    main()
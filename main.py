def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    wordOccurances = findEachLetterOccurance(text)
    print(f"--- Begin report of {book_path}---")
    print("-----------------------------------")
    print(f"{num_words} words found in the document")
    print("-----------------------------------")
    for x, y in wordOccurances:
        print(f"The {x} character was {y} found times.")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def findEachLetterOccurance(text):
    text = text.lower()
    character_count = {}

    for char in text:
        if char.isalpha():
            if char not in character_count:
                character_count[char] = 1
            else:
                character_count[char] += 1

    sorted_count = sorted(character_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_count


main()
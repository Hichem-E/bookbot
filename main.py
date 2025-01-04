def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = word_count(book)
    char_d = get_chars_dict(book)
    char_list_sorted = d_to_sorted_list(char_d)
    
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    print()

    for d in char_list_sorted:
        if d["letter"].isalpha():
            print(f"The {d["letter"]} character was found {d["count"]} times")
    
    print("--- End report ---")



def d_to_sorted_list(char_d):
    list_of_letters = []
    for k, v in char_d.items():
        list_of_letters.append({"letter": k, "count": v})
    
    list_of_letters.sort(key=lambda x: x.get("count"), reverse=True)
    return list_of_letters

    
def word_count(text):
    word_count = len(text.split())
    return word_count

def get_chars_dict(text):
    lowercase_file = text.lower()
    letter_count = {}

    for letter in lowercase_file:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
            # letter_count.get(letter, 0) + 1
    return letter_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
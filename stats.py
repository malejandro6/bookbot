def word_count(book):
    return len(book.split())

def character_count(book_text):
    book_text = book_text.lower()
    char_counts = {}
    for char in book_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sort_characters(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        chars_list.append({"char": char, "num": count})
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list


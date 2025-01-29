def count_characters(text):
    char_count = {} 
    for char in text:
        if char.isalpha():
            lowercase_char = char.lower()
            if lowercase_char in char_count:
                char_count[lowercase_char] = char_count[lowercase_char] + 1
        else:
            char_count[lowercase_char] = 1
    return char_count
    
def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["count"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        char_list = []
        for char, count in char_count.itmes():
            char_list.append({"char": char, "count": count})
        char_list.sort(reverse=True, key=sort_on)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for char_dict in char_list:
            print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
        print("---End report ---")
        print(word_count)
        print(char_count)
        print(char_list)

if __name__ == "__main__":
    main()


def count_characters(text):
    char_count = {} 
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_count:
            char_count[lowercase_char] = char_count[lowercase_char] + 1
        else:
            char_count[lowercase_char] = 1
    return char_count
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        print(word_count)
        print(char_count)

if __name__ == "__main__":
    main()


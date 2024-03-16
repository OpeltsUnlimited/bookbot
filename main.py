def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = countWords(file_contents)
        letter_count = countLetters(file_contents)
        letter_count_sortet = sortLetterGroups(letter_count)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print() # empty line
        print_letter_lines(letter_count_sortet)
        print("--- End report ---")

def countWords(text):
    words = text.split()
    return len(words)

def countLetters(text):
    lowered_string = text.lower()
    wordcounts = {}
    for letter in lowered_string:
        if not letter in wordcounts:
            wordcounts[letter] = 0
        wordcounts[letter] += 1
    return wordcounts

def sortLetterGroups(letter_dict):
    list_letter_count = [{"letter":key, "count":value} for key, value in letter_dict.items()] # List Comprehension
    def sort_on(dict):
        return dict["count"]
    list_letter_count.sort(reverse=True, key=sort_on)
    return list_letter_count

def print_letter_lines(sorted_letters):
    for dict in sorted_letters:
        print(f"The {dict["letter"]} character was found {dict["count"]} times")

if __name__ == "__main__":
    main()
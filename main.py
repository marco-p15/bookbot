def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_all(file_contents)

def words(file_contents):
    w = 0

    file_words = file_contents.split()

    for word in file_words:
        w+=1

    return w

def characters(file_contents):
    low_f_contents = file_contents.lower()

    chars = {}

    for word in low_f_contents:
        if word.isalpha():
            if word not in chars:
               chars[word] = 0
            chars[word] += 1

    list_chars = list(chars.items())
    list_chars.sort(reverse=True, key=lambda x: x[1])        

    for key, value in list_chars:
        print(f"The {key} character was found {value} times")
    
    return chars

def print_all(file_contents):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words(file_contents)} words found in the document")
    print("")
    characters(file_contents)
    print("--- End report---")  

main()
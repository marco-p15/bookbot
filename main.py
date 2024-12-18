def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        words(file_contents)
        characters(file_contents)

def words(file_contents):
    w = 0

    file_words = file_contents.split()

    for word in file_words:
        w+=1

    print(f"Words: {w}")

def characters(file_contents):
    low_f_contents = file_contents.lower()

    chars = {}

    for word in low_f_contents:
        if word not in chars:
           chars[word] = 0
        chars[word] += 1

    print(f"Characters: {chars}")

main()
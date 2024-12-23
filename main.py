# bookbot project

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)
    print(len(file_contents.split()))

    char_counts = {}
    for char in file_contents.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    print(char_counts)



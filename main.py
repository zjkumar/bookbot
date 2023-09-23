with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)

def count_words(file_contents):
    words = file_contents.split()
    count = 0
    for word in words:
        count+=1
    print(count)

count_words(file_contents)
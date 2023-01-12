from typing import List
import string

def count_words(file_path:str, word:str):
    with open(file_path, 'r') as f:
        text = f.read()
    text = text.translate(str.maketrans('', '', string.punctuation)).lower() # remove punctuation and sets all letters to lowercase
    word_list = text.split()
    return word_list.count(word)

def readlines(filename:str) -> List[str]:
    with open(filename, "r") as f:
        lines = [line.strip()for line in f.readlines()]

    return lines

def main():
    filename = "file.txt"
    lines = readlines(filename)
    count = {}
    for line in lines:
        for word in line.split(" "):
            word = word.translate(str.maketrans("","",string.punctuation))
            count[word.lower()] = 0

    for word in count.keys():
        count[word] = count_words(filename, word)
    count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

    for k,v in count.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
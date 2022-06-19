import json

data = json.load(open("data.json"))


def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    else:
        return "non-existant"


word = input("enter word: ")
print(translate(word))

import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word.lower(), data.keys())) > 0:
        yn = input("did you mean %s ? Enter Y if yes else enter N: " %
                   get_close_matches(word.lower(), data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word.lower(), data.keys())[0]]
        elif yn == 'N':
            return "word non-existant"
        else:
            return "entry not valid"

    else:
        return "non-existant"


word = input("enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

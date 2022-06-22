import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    if word.lower() in data:
        return data[word.lower()]
    elif len(get_close_matches(word.lower(), data.keys())) > 0:
        return "did you mean %s ?" % get_close_matches(word.lower(), data.keys()[0])
    else:
        return "non-existant"


word = input("enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

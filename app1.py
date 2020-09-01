import json
from difflib import get_close_matches
data = json.load(open("original\data.json"))

def translate(word):
    word = word.lower() 
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn= input("Did you mean %s instead? Enter Y if Yes, or N if No: " %get_close_matches(word,data.keys())[0] ) 
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn == "N":
            return "Word doesn't exist. Please double check it"
        else:
            return "Didn't understand your entry"
    else:
        return "Word doesn't exist"


#global variable
word = input("Enter word:")

print(translate(word))
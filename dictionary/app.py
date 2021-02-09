import json 
import difflib
from difflib import get_close_matches
data = json.load(open('data.json'))
def translate(w):
    #to convert every input to lower case
    w=w.lower()

    if w in data:
        return data[w]
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input ("Did you mean %s instead? Enter Y if Yes, or N if no. " %get_close_matches(w,data.keys())[0])
        if yn=="Y" or yn=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N" or yn=="n":
            return("The word doesn't exist. Please double check it")
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it"
word=input("Enter the word: ")

output=(translate(word))

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)

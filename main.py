import requests
from bs4 import BeautifulSoup
import re

count = input("Number of words to return (Enter to use default): ")
if count == "":
    count = 10
else:
    count = int(count)
excluded_words = input("Words to exclude: ")
if excluded_words != "":
    excluded_words = re.sub("[^\w]", " ", excluded_words).split()

text = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/Microsoft').content, 'html.parser').text
section = re.sub("[^\w]", " ", re.search(r'(?s)History(\r\n|\r|\n)Main article(.*)Corporate affairs', text).group(0).replace("Corporate affairs", "")).split()
words = {}
for w in section:
    if w not in excluded_words:
        if w in words:
            words[w] += 1
        else:
            words[w] = 1

words = sorted(words.items(), key=lambda item: item[1], reverse=True)

print(f"{'':<10} # of occurrences")
for k,v in words[:count]:
    print(f"{k:<10} {v}")
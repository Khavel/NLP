from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize
from urllib import urlopen

url = "http://norvig.com/ngrams/spell-errors.txt"
response = urlopen(url)

misspellings = {}
leftLetters = {}

for line in response:
    initial = ''
    words = set([])
    for word in line.split():
        if word[-1] == ':':
            initial = word[:-1]
        else:
            words.add(word)
    misspellings.update({initial:words})

for w1 in misspellings:
    w1List = list(w1)
    leftLetters.update({w1,set([])})
    for w2 in misspellings[w1]:
        w2List = list(w2)
        lIndex = 0
        for letter1 in w1w1List:
            for letter2 in w2List:
                if letter1 == letter2:
                    break;
                else:
                    lIndex = lIndex + 1
                
            leftLetters[w1].add(lIndex)

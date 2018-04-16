import nltk
from nltk import *
from nltk.corpus import gutenberg

text = gutenberg.words(fileids='austen-emma.txt')
freq = FreqDist(text)

freqDic = {}
for word in text:
    if not freqDic.has_key(word):
        freqDic.update({word:freq[word]})

unigramDic = {}
textLen = len(text)

for i in range(len(text)):
    w0 = text[i]
    if not unigramDic.has_key(w0):
        unigramDic.update({w0:freq[w0]/(textLen*1.0)})
P = 1.0
for i in range(len(text)):
    P = P * unigramDic[text[i]]
print P

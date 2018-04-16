import nltk
from nltk.corpus import brown
import collections

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words(categories="news"))
tagged_text = nltk.pos_tag(text)
tags = []

for w in tagged_text:
    tags.append(w[1])

fDist = nltk.FreqDist(tags)
mostCommon = fDist.most_common(20)
for t in mostCommon:
    print nltk.help.upenn_tagset(t[0])

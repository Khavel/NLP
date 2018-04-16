import nltk
from nltk.corpus import brown
import collections

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words(categories="news"))
tagged_text = nltk.pos_tag(text)
maxTags = ["test",set([])]
dictTags = collections.defaultdict(set)
for w in tagged_text:
    dictTags[w[0]].add(w[1])

for w in dictTags:
    if len(dictTags[w]) > len(maxTags[1]):
        maxTags = [w,dictTags[w]]
print maxTags

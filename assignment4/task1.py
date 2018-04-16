import nltk
from nltk.corpus import brown

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words(categories="government"))
tagged_text = nltk.pos_tag(text)
nounsPlural = []
nounsSingular = []
for w in tagged_text:
    if w[1] == "NN" and len(w[0])>1:
        if w[0][-1] == "s":
            if not w[0][-2] == "'":
                nounsPlural.append(w[0])
        else:
            nounsSingular.append(w[0])
commonPlurals = []
nounsPlural = sorted(nounsPlural)
nounsSingular = sorted(nounsSingular)
for w in nounsSingular:
    ws = w
    ws = ws + 's'
    if ws in nounsPlural:
        commonPlurals.append(w)

freq = nltk.FreqDist(commonPlurals)
print freq.most_common(20)

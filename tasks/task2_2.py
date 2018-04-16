import nltk
from nltk.corpus import brown
import matplotlib.pyplot as plt


cfd = nltk.ConditionalFreqDist((genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
i = 1
xAxis = []
yAxis = []
for word in cfd['romance'].most_common(len(cfd['romance'])):
    xAxis.append(i)
    yAxis.append(word[1])
    i = i+1

plt.ylabel('Frequency')
plt.xlabel('Rank')
plt.plot(xAxis,yAxis)
plt.yscale('log')
plt.grid(True)
plt.show()

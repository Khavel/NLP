import math, collections

class CustomLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.unigramCounts = collections.defaultdict(lambda: 1)
    self.timesSeen = collections.defaultdict(set) #This dictionary's keys are the number of times a word appears on the training text, and as values it has a set with the words appearing said number of times.
    self.timesSeenOrder = collections.defaultdict(int) #This dictionary's keys are the number of times a word appears on the training text, and as values it has the position of that number in the sorted list.
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model.
        Compute any counts or other corpus statistics in this function.
    """
    for sentence in corpus.corpus:
      for datum in sentence.data:
        token = datum.word
        self.unigramCounts[token] += 1
        self.total += 1

    self.listOfCounts = list() #This list will contain all of the words counts to sort them
    for token in self.unigramCounts:
      count = self.unigramCounts[token]
      if not self.timesSeen.has_key(count):
          self.listOfCounts.append(count)
      self.timesSeen[count].update({token})

    self.listOfCounts.sort()

    #Once the list is sorted, all the items inside are put in a dictionary, mapped to their corresponding position.
    for i in range(len(self.listOfCounts)):
        self.timesSeenOrder[self.listOfCounts[i]] = i+1




  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0
    for token in sentence:
        if not self.unigramCounts.has_key(token):
            score += math.log(self.listOfCounts[0])
            score -= math.log(self.total)
        else:
            cPosition = self.timesSeenOrder[self.unigramCounts[token]+1]
            score += math.log(self.unigramCounts[token]+1)
            score += math.log(self.listOfCounts[cPosition])
            score -= math.log(2*self.listOfCounts[cPosition-1])
    return score

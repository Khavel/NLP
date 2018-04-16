import math, collections

class StupidBackoffLanguageModel:

  def __init__(self, corpus):
    """Initialize your data structures in the constructor."""
    self.bigramCounts = collections.defaultdict(lambda: 0)
    self.unigramCounts = collections.defaultdict(lambda: 1)
    self.total = 0
    self.vocab = set([])
    self.train(corpus)

  def train(self, corpus):
    """ Takes a corpus and trains your language model.
        Compute any counts or other corpus statistics in this function.
    """
    for sentence in corpus.corpus:
      datumBefore = 0
      for datum in sentence.data:
        self.unigramCounts[datum.word] = self.unigramCounts[datum.word] + 1
        if not datumBefore == 0:
            token = (datumBefore.word,datum.word)
            self.bigramCounts[token] = self.bigramCounts[token] + 1
            self.total += 1
        datumBefore = datum
        self.vocab.add(datum.word)

  def score(self, sentence):
    """ Takes a list of strings as argument and returns the log-probability of the
        sentence using your language model. Use whatever data you computed in train() here.
    """
    score = 0.0

    datumBefore = 0
    for datum in sentence:
      countUnigram = self.unigramCounts[datum]
      if not datumBefore == 0:
          token = (datumBefore,datum)
          countBigram = self.bigramCounts[token]
          if countBigram > 0:
            score += math.log(countBigram)
            score -= math.log(self.unigramCounts[datumBefore])
          else:
            score += math.log(0.4)
            score += math.log(countUnigram)
            score -= math.log(self.total)

      datumBefore = datum
    return score

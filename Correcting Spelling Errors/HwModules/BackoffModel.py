import math, collections
from  SmoothUnigramModel import SmoothUnigramModel

class BackoffModel:

    def __init__(self, corpus):
        """Initialize your data structures in the constructor."""
        self.total = 0
        self.unigramCounts = collections.defaultdict(lambda: 0)
        self.bigramCounts = collections.defaultdict(lambda: 0)
        self.train(corpus)


    def train(self, corpus):
        """ Takes a corpus and trains your language model.
            Compute any counts or other corpus statistics in this function.
        """
        # TODO your code here
        # Tip: To get words from the corpus, try
        #    for sentence in corpus.corpus:
        #       for datum in sentence.data:
        #         word = datum.word
        for sentence in corpus.corpus:
            token = sentence.data[0].word
            self.unigramCounts[token] += 1
            self.total += 1
            for i in xrange(1, len(sentence.data)):
                nextToken = sentence.data[i].word
                self.unigramCounts[nextToken] += 1
                self.bigramCounts[(token, nextToken)] += 1
                token = nextToken
                self.total += 1

        self.unigramCounts['UNK'] = 0


    def score(self, sentence):
        """ Takes a list of strings as argument and returns the log-probability of the
            sentence using your language model. Use whatever data you computed in train() here.
        """
        # TODO your code here
        score = 0.0
        token = sentence[0]
        for i in xrange(1, len(sentence)):
            nextToken = sentence[i]
            count = self.bigramCounts[(token, nextToken)]
            if count > 0:
                score += math.log(count)
                score -= math.log(self.unigramCounts[token])
            else:
                count = self.unigramCounts[nextToken]
                if count > 0:
                    score += math.log(self.unigramCounts[nextToken] + 1)
                    score -= math.log(self.total + len(self.unigramCounts))
                else:
                    score += math.log(1.0 / (self.total + len(self.unigramCounts)))
            token = nextToken

        return score
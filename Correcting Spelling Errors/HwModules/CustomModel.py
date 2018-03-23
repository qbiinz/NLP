import math, collections


class CustomModel:

    def __init__(self, corpus):
        """Initial custom language model and structures needed by this mode"""
        self.total = 0
        self.absDiscount = .75
        self.discount = .4
        self.unigramCounts = collections.defaultdict(lambda: 0)
        self.bigramCounts = collections.defaultdict(lambda: 0)
        self.trigramCounts = collections.defaultdict(lambda: 0)
        self.train(corpus)
        self.counter = 0

    def train(self, corpus):
        """ Takes a corpus and trains your language model.
        """
        # TODO your code here
        for sentence in corpus.corpus:
            token1 = sentence.data[0].word
            token2 = sentence.data[1].word
            self.unigramCounts[token1] += 1
            self.unigramCounts[token2] += 1
            self.bigramCounts[(token1, token2)] += 1
            self.total += 2
            for token in sentence.data[2:]:
                token3 = token.word
                self.unigramCounts[token3] += 1
                self.bigramCounts[(token2, token3)] += 1
                self.trigramCounts[(token1,token2,token3)] += 1
                token1 = token2
                token2 = token3
                self.total += 1

        self.unigramCounts['UNK'] = 0

    def score(self, sentence):
        """ With list of strings, return the log-probability of the sentence with language model. Use
            information generated from train.
        """
        # TODO your code here
        score = 0.0
        token1 = sentence[0]
        token2 = sentence[1]
        for i in xrange(2, len(sentence)):
            token3 = sentence[i]
            count3 = self.trigramCounts[(token1, token2, token3)]
            count2 = self.bigramCounts[(token1, token2)]
            if count3 > 0 :
                score += math.log(count3)
                score -= math.log(count2)
            else:
                count2 = self.bigramCounts[(token2, token3)]
                count1 = self.unigramCounts[token2]
                if count2 > 0 :
                    score += math.log(count2)
                    score -= math.log(count1)
                else:
                    count = self.unigramCounts[token3]
                    if count > 0:
                        score += math.log(count + 1)
                        score -= math.log(self.total + len(self.unigramCounts))
                    else:
                        score += math.log(1.0 / (self.total + len(self.unigramCounts)))
            token1 = token2
            token2 = token3
        return score

import re
import math
#grab probabilities from entropy.txt
probs = re.compile("(\S*)\s(\S*)\s(\S*).*$")

sentEntr = []
sentCounter =0
with open('entropy.txt', 'r') as entropy:
    for line in entropy:
        found = probs.match(line)
        #sentence probability
        sentEntr.append(float(found.group(2)))
        sentCounter += 1

prob = 0
for num in sentEntr:
    prob += -math.log2(num)

prob /= sentCounter

print(prob)

#72.03295
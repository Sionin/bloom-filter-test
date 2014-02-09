#!/usr/bin/env python
from cmath import log
import random
import string

from bloom import BloomFilter

MAX_SIZE = 100
ERROR_PROBABILITY = 0.0000001


def generateValue(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))


def generateOther():
    return generateValue(10, string.ascii_lowercase + string.digits)


size = -(MAX_SIZE * log(ERROR_PROBABILITY)) / (log(2) * log(2))
count = (size / MAX_SIZE) * log(2)

optimalSize = int(complex(size).real)
optimalCount = int(complex(count).real)

print optimalSize, optimalCount

bloom = BloomFilter(optimalSize, optimalCount)

falsePositive = False
inserted = 0;
falseValue = "";

while not falsePositive:

    for i in range(MAX_SIZE / 100):
        bloom.add(generateValue())
        inserted += 1
    print(bloom)

    for i in range(MAX_SIZE / 100):
        falseValue = generateOther()
        falsePositive = (falseValue in bloom)
        if falsePositive:
            break;

print "========================="
print "False positive at '", falseValue, "' after ", inserted, " insertions"



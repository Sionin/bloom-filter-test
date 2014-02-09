#!/usr/bin/env python
from random import shuffle

from bitset import Bitset

PRIMES = [13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67,
          71, 73, 79, 83, 89, 97, 101,
          103, 107, 109, 113, 127,
          131, 137, 139, 149, 151, 157
]
shuffle(PRIMES)


class BloomFilter:
    def hash(self, string, prime):
        h = 0
        for c in string:
            h = (prime * h + ord(c)) & 0xFFFFFFFF
        bitset_length = (((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000)
        return bitset_length % self.bitset.length

    def hashFunctions(self, primes):
        result = list()
        for p in primes:
            print "lambda x: self.hash(x, ", p, ")"
            result.append(lambda x: self.hash(x, p))
        return result

    def __init__(self, size, hashCount=0):
        self.bitset = Bitset(0, size)
        self.hashs = self.hashFunctions(PRIMES[0:hashCount or len(PRIMES)])
        pass

    def __str__(self):
        return "BloomFilter[size={} value={}]".format(self.bitset.length, self.bitset.__str__())

    def __contains__(self, item):
        contains = True
        for h in self.hashs:
            contains = contains & self.bitset[h(item)]
            if not contains:
                break
        return contains

    def add(self, item):
        for h in self.hashs:
            self.bitset[h(item)] = True

    def remove(self, item):
        for h in self.hashs:
            self.bitset[h(item)] = False

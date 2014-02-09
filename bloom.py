#!/usr/bin/env python

from bitset import Bitset

__author__ = 'sergei'


class BloomFilter:
    def hash(self, string, prime):
        h = 0
        for c in string:
            h = (prime * h + ord(c)) & 0xFFFFFFFF
        bitset_length = (((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000)
        return bitset_length % int(self.bitset.length)

    def __init__(self, size, hashCount=0):
        self.bitset = Bitset(0, size)
        #2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157
        hashFunctions = [
            (lambda x: self.hash(x, 13))
            , (lambda x: self.hash(x, 17))
            , (lambda x: self.hash(x, 19))
            , (lambda x: self.hash(x, 23))
            , (lambda x: self.hash(x, 29))
            , (lambda x: self.hash(x, 31))
            , (lambda x: self.hash(x, 37))
            , (lambda x: self.hash(x, 41))
            , (lambda x: self.hash(x, 47))
            , (lambda x: self.hash(x, 53))
            , (lambda x: self.hash(x, 59))
            , (lambda x: self.hash(x, 61))
            , (lambda x: self.hash(x, 67))
            , (lambda x: self.hash(x, 71))
            , (lambda x: self.hash(x, 73))
            , (lambda x: self.hash(x, 79))
            , (lambda x: self.hash(x, 83))
            , (lambda x: self.hash(x, 89))
            , (lambda x: self.hash(x, 97))
            , (lambda x: self.hash(x, 101))
        ]
        self.hashs = hashFunctions[0:hashCount or len(hashFunctions)]
        pass

    def __str__(self):
        return "BloomFilter[size={} value={}]".format(self.bitset.length, self.bitset.__str__())

    def __contains__(self, item):
        contains = True
        for h in self.hashs:
            contains = contains & self.bitset[h(item)]
        return contains

    def add(self, item):
        for h in self.hashs:
            self.bitset[h(item)] = True

    def remove(self, item):
        for h in self.hashs:
            self.bitset[h(item)] = False

#!/usr/bin/env python

from bitset import Bitset

__author__ = 'sergei'


class BloomFilter:

    def __init__(self, size):
        self.bitset = Bitset(0, size)
        pass

    def __contains__(self, item):
        return self.bitset[self.hash1(item)] & self.bitset[self.hash2(item)] & self.bitset[self.hash3(item)] & self.bitset[self.hash4(item)] & self.bitset[self.hash5(item)]

    def add(self, item):
        self.bitset[self.hash1(item)] = True
        self.bitset[self.hash2(item)] = True
        self.bitset[self.hash3(item)] = True
        self.bitset[self.hash4(item)] = True
        self.bitset[self.hash5(item)] = True

    def remove(self, item):
        self.bitset[self.hash1(item)] = False
        self.bitset[self.hash2(item)] = False
        self.bitset[self.hash3(item)] = False
        self.bitset[self.hash4(item)] = False
        self.bitset[self.hash5(item)] = False

    def hash1(self, string):
        return self.hash(string, 13)

    def hash2(self, string):
        return self.hash(string, 17)

    def hash3(self, string):
        return self.hash(string, 31)

    def hash4(self, string):
        return self.hash(string, 41)

    def hash5(self, string):
        return self.hash(string, 59)

    def hash(self, string, prime):
        h = 0
        for c in string:
            h = (prime * h + ord(c)) & 0xFFFFFFFF
        bitset_length = (((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000)
        return bitset_length % int(self.bitset.length)
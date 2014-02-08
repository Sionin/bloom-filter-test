#!/usr/bin/env python
import random
import string

from bloom import BloomFilter


def generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))

bloom = BloomFilter(10000)
print bloom.bitset

for i in range(1000):
    bloom.add(generator())

print bloom.bitset

print("MyString1" in bloom)







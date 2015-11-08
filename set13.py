#Single-byte XOR cipher

#from collections import Counter
import sys
import crypto
#import textutils
#import profile
from collections import defaultdict
from operator import itemgetter, attrgetter, methodcaller
import binascii

prob = [
    ('a', 0.0651738),
    ('b', 0.0124248),
    ('c', 0.0217339),
    ('d', 0.0349835),
    ('e', 0.1041442),
    ('f', 0.0197881),
    ('g', 0.0158610),
    ('h', 0.0492888),
    ('i', 0.0558094),
    ('j', 0.0009033),
    ('k', 0.0050529),
    ('l', 0.0331490),
    ('m', 0.0202124),
    ('n', 0.0564513),
    ('o', 0.0596302),
    ('p', 0.0137645),
    ('q', 0.0008606),
    ('r', 0.0497563),
    ('s', 0.0515760),
    ('t', 0.0729357),
    ('u', 0.0225134),
    ('v', 0.0082903),
    ('w', 0.0171272),
    ('x', 0.0013692),
    ('y', 0.0145984),
    ('z', 0.0007836),
    (' ', 0.1918182)
]

hexa = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
string = binascii.unhexlify(hexa)

def letters_freqs(string, top=100):
    counts = defaultdict(int)
    for x in string:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


def replace_string(string):
	prob_order = sorted(prob, key=itemgetter(1), reverse=True)
	freqs = letters_freqs(string)
	
	i=0	
	for x in freqs:
		string= string.replace(x[0][0],prob_order[i][0])
		i=i+1
	return string


if __name__ == '__main__':
	encodedS = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	s = binascii.unhexlify(encodedS)
	
	#print replace_string(encodedS)

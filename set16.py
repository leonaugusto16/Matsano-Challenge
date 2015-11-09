def hamming_distance_bin(string1,string2):
	s1 = bytearray(string1)
	s2 = bytearray(string2)

	return sum(bin(i^j).count("1") for i,j in zip(s1,s2))

if __name__ == '__main__':
	print hamming_distance_bin('this is a test','wokka wokka!!!')

def equality(text,key):
	string = []
        i=0
        while(i<len(text)):
                string.append(key)
                i=i+len(key)
        string=''.join(string)
        
        if (len(text)<len(string)):
                string = string[:len(text)]
        return string   	

def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

if __name__ == '__main__':

	arquivo = open('5.txt','r')
	text = arquivo.readlines()

	i=0
	while(i<len(text)):
		
		key = "ICE"
		key_len_text = equality(text[i],key)
		r = xor_strings(text[i],key_len_text).encode("hex")
		i=i+1
		print r
		
		

import binascii,sys
#list words in english http://www.englishexperts.com.br/forum/1000-palavras-mais-usadas-em-ingles-t4469.html
keywords=['the', 'of', 'to', 'and', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'I', 'his', 'they', 'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'hot', 'word', 'but', 'what', 'some', 'we', 'can', 'out', 'other', 'were', 'all', 'there', 'when', 'up', 'use', 'your', 'how', 'said', 'an', 'each', 'she', 'wich', 'do', 'their', 'time', 'if', 'will', 'way', 'about', 'many', 'then', 'them', 'write', 'would', 'like', 'so', 'these', 'her', 'long', 'make', 'thing', 'see', 'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did', 'number', 'sound', 'no', 'most', 'people', 'my', 'over', 'know', 'water', 'than', 'call', 'first', 'who', 'may', 'down', 'side', 'been', 'now', 'find']

def decrypt(encoded,key):
    xor=lambda x ,y :int(x,16)^int(y,16)
    ans=""
    for temp in [encoded[a:a+2] for a in range(0,len(encoded)-1,2)]:
        ans=ans+chr(xor(temp,key))
    return ans
       

def brute_xor(encoded):
   
    hex_key="0"

    #100 most frequently used words in the English, we scan the text looking for them, this indicates a high probability the correct phrase
    for a in range(0,255):
        ans=decrypt(encoded,hex_key)
        for word in keywords:
	    word = " "+word+" "
            if word in ans or word+" " in ans or " "+word in ans or " "+word+" " in ans:
		print "[*]Encrypted data : "+linha[i]
		print "[+]Starting Decrpytion ...\n"
		print "[*]Decrypted data : "+ans
                print "[*]key : 0x"+(hex_key)
		print "[*]Word Denounced : "+word
		break
	
	#Increment key hex
	int_key=int(hex_key,16)
    	int_key=int_key+1
    	hex_key=hex(int_key)[2:]


if __name__ == '__main__':
	
	arquivo = open('4.txt','r')
	linha = arquivo.readlines()
	i=0
	while(i<len(linha)):
        	brute_xor(linha[i])
		i=i+1

        print "\n[+] Done\n"

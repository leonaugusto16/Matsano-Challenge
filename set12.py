# Fixed XOR

a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

# Primeiramente decodificamos nossa string em hexa
binary_a = a.decode("hex")
binary_b = b.decode("hex")

# Agora temos a funcao que transforma cada caracter em um numero (xor so pode ser usado em numeros)
# depois transformamos o resultado da operacao em carateres, repetindo ate o fim da string.
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

# Encodamos novamente para termos o valor da nova string
r = xor_strings(binary_a, binary_b).encode("hex")
print r

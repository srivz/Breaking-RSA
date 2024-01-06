from itertools import product


def mod_pow(base, exponent, mod):
    power = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            power = (power * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return power


def encrypt(public_key, pq, message, chk_msg):
    hex_chunks = (message.encode('utf-8').hex())
    num = (int(hex_chunks, 16))
    msg = mod_pow(num, public_key, pq)
    if msg == int(chk_msg):
        print(message, end="")


# This only works when:
# The plain text is divided into x chunks and converted into hex-value then into decimal.
# This decimal value is encrypted with public key of friend.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 .,?!\0"
chunk_size = int(input("Enter chunk_size: "))
combinations = [''.join(p) for p in product(characters, repeat=chunk_size)]
cipher_message = input("Enter your cipher text: ")
e = input("Enter e used to encrypt: ")
n = input("Enter n used to encrypt: ")
num_chunks = cipher_message.strip("[] ").split(",")
for x in num_chunks:
    for i in combinations:
        encrypt(e, n, i, x)

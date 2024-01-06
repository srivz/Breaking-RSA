import random
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def mod_inverse(t, e, p, q, r, count):
    new_p = q
    new_q = p - (q * r)
    new_r = t // e
    modulus = t % e
    if modulus == 1:
        return new_p - (new_q * new_r)
    else:
        return mod_inverse(e, modulus, new_p, new_q, new_r, count + 1)


def find_private_key(t, key):
    d = mod_inverse(t, key, 1, 0, -1, 0)
    if d < 0:
        d = d % t
    print("Your Private-keys is:", d)


def is_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1


def ce(t):
    print("Possible Values of Public-key(e) are:")
    lower = 2
    upper = t - 1
    i = 0
    while i < 10:
        random_e = random.randint(lower, upper)
        if is_prime(random_e) and is_coprime(random_e, t):
            print(random_e, end="\t")
            i += 1


def mod_pow(base, exponent, mod):
    power = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            power = (power * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return power


def encrypt(n, public_key, message):
    result = []
    chunks = [message[i:i + 3] for i in range(0, len(message), 3)]
    print(chunks)
    hex_chunks = []
    for word in chunks:
        hex_chunks.append(word.encode('utf-8').hex())
    print(hex_chunks)
    num_chunks = []
    for hex_num in hex_chunks:
        num_chunks.append(int(hex_num, 16))
    print(num_chunks)
    for text_num in num_chunks:
        x = mod_pow(text_num, public_key, n)
        result.append(x)
    print("\nTHE ENCRYPTED MESSAGE IS")
    print(', '.join(map(str, result)))


def decrypt(n, private_key, message):
    msg = [int(x) for x in message.split(',')]
    print(msg)
    x = []
    for num in msg:
        x.append(mod_pow(num, private_key, n))
    print(x)
    hex_num = []
    for num in x:
        hex_num.append(hex(num)[2:].upper())
    print(hex_num)
    result = []
    for word in hex_num:
        result.append(bytes.fromhex(word).decode('utf-8'))
    print(result)
    print("\nTHE DECRYPTED MESSAGE IS")
    print("".join(result))


def sign(n, private_key, name):
    result = []
    chunks = [name[i:i + 3] for i in range(0, len(name), 3)]
    hex_chunks = []
    for word in chunks:
        hex_chunks.append(word.encode('utf-8').hex())
    num_chunks = []
    for hex_num in hex_chunks:
        num_chunks.append(int(hex_num, 16))
    for text_num in num_chunks:
        x = mod_pow(text_num, private_key, n)
        result.append(x)
    print("\nYOUR DIGITAL SIGNATURE IS")
    to_print = ', '.join(map(str, result))
    print(to_print)


def verify_sign(n, public_key, signature, sender):
    msg = [int(x) for x in signature.split(',')]
    x = []
    for num in msg:
        x.append(mod_pow(num, public_key, n))
    hex_num = []
    for num in x:
        hex_num.append(hex(num)[2:].upper())
    result = []
    for word in hex_num:
        result.append(bytes.fromhex(word).decode('utf-8'))
    if "".join(result) == sender:
        print("\nTHE SIGNATURE IS VALID.")


def generate_random_prime(num=None):
    while True:
        random_n = random.randint(32768, 65535)
        if is_prime(random_n) and random_n != num:
            return random_n


def get_prime(prompt, exclusion=None):
    while True:
        p = int(input(prompt))
        if p == exclusion:
            print("\nSelect a prime different from p!!!")
            help_choice = input("Do you need help generating a prime number (y/n)? ")
            if help_choice.lower() == "y":
                num = generate_random_prime(exclusion)
                print("p=", num)
                return num
            else:
                continue
        elif p < 32768 or p > 65535 or not is_prime(p):
            print("\nEnter a prime number between 32768 to 65535!!")
            help_choice = input("Do you need help generating a prime number (y/n)? ")
            if help_choice.lower() == "y":
                num = generate_random_prime()
                print("p=", num)
                return num
            else:
                continue
        else:
            return p


def main():
    choice = input("\nDo you want to get a new key(k) or encrypt(e) or decrypt(d) or sign(s) or verify a signature("
                   "v)?\n")
    while choice != 'k' and choice != 'e' and choice != 'd' and choice != 's' and choice != 'v':
        print("Invalid choice. Please choose 'p' to generate a new key, 'e' to encrypt, or 'd' to decrypt, or 's' to "
              "sign, or 'v' to verify a signature.")
        choice = input("Do you want to get a new key(p) or encrypt(e) or decrypt(d) or sign(s) or verify a signature("
                       "v)?\n")
    if choice == 'k':
        p = get_prime("\nEnter p: ")
        q = get_prime("\nEnter q: ", p)
        if q < 32768 or q > 65535 or not is_prime(q) or p == q:
            print("\nEnter a prime number between 32768 to 65535!!")
            help_choice = input("Do you need help assigning a prime number (y/n)? ")
            if help_choice.lower() == "y":
                generate_random_prime()
            else:
                print("\nOkay!!\n")
            q = int(input("\nEnter q: "))
        n = p * q
        print("\nValue of N is:", n)
        phi_n = (p - 1) * (q - 1)
        print("\nPhi(N) is:", phi_n)
        ce(phi_n)
        public_key = int(input("\nSelect a Public-key Number: "))
        print("\nYour Public-key(e, N) is: ({}, {})".format(public_key, n))
        find_private_key(phi_n, public_key)
    elif choice == 'e':
        public_key, n = map(int, input("\nEnter your Partner's Public-key{e, N} here:\n").strip(" ").split(','))
        message = input("\nEnter your Plain Text here:\n")
        encrypt(n, public_key, message)
    elif choice == 'd':
        private_key, n = map(int, input("\nEnter your Private-key{d, N} here:\n").strip(" ").split(','))
        message = input("\nEnter your Partner's Cipher Text here:\n").strip("[ ]")
        decrypt(n, private_key, message)
    elif choice == 's':
        private_key, n = map(int, input("\nEnter your Private-key{d, N} here:\n").strip(" ").split(','))
        message = input("\nEnter your name here:\n")
        sign(n, private_key, message)
    elif choice == 'v':
        public_key, n = map(int, input("\nEnter your Partner's Public-key{e, N} here:\n").strip(" ").split(','))
        signature = input("\nEnter your partner's signature here:\n").strip("[ ]")
        name = input("\nEnter your partner's name here:\n")
        verify_sign(n, public_key, signature, name)
    else:
        print("\nUnknown choice!!")


if __name__ == "__main__":
    main()


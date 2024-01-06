def mod_inverse(t, power, a=1, b=0, c=-1):
    na, nb, nc = b, a - b * c, t // power
    mod = t % power
    return na - nb * nc if mod == 1 else mod_inverse(power, mod, na, nb, nc)


def find_d(t, key):
    p_key = mod_inverse(t, key)
    if p_key < 0:
        p_key = p_key % t
    return p_key


def factorize(x):
    prime = []
    c = 0
    for i in range(2, x + 1):
        if x % i == 0:
            prime.append(i)
            c = c + 1 
            if c == 2:
                break
    return prime[0], prime[1]


# Should know N,e
n = int(input("Enter N: "))
p, q = factorize(n)
print("p=", p, ", q=", q)
print("n=", n, "phi(n)=", (p-1)*(q-1))
e = int(input("Enter E: "))
d = find_d((p-1)*(q-1), e)
print("d=", d)

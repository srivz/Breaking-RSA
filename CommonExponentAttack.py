def mod_inverse(mod, text, p=1, q=0, r=-1, count=0):
    new_p, new_q, new_r, modulus = q, p - (q * r), mod // text, mod % text
    if modulus == 1:
        return new_p - (new_q * new_r)
    else:
        return mod_inverse(text, modulus, new_p, new_q, new_r, count + 1)


def is_coprime(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1 == 1


def mod_pow(base, exponent, mod):
    power = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            power = (power * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return power


# Should know 2 intercepts(C, e) with same n and message.
n = 143
intercepts = [[42, 7], [9, 17]]
# n = int(input("Enter n: "))
# intercepts = []
# for i in range(0, 2):
#     print("Enter intercept ", i+1)
#     c = int(input("Enter C: "))
#     e = int(input("Enter e: "))
#     intercepts.append([c, e])
if is_coprime(intercepts[0][1], intercepts[1][1]):
    a = mod_inverse(intercepts[1][1], intercepts[0][1])
    if a < 0:
        a = a % intercepts[1][1]
    b_inv = mod_inverse(intercepts[0][1], intercepts[1][1])
    b = b_inv
    M1, M2 = 0, 0
    if a < 0:
        M1_pow = mod_pow(intercepts[0][0], a, n)
        M1 = mod_inverse(n, M1_pow)
        if M1 < 0:
            M1 = M1 % n
    else:
        M1 = mod_pow(intercepts[0][0], a, n)
    if b < 0:
        M2_pow = mod_pow(intercepts[1][0], -b, n)
        M2 = mod_inverse(n, M2_pow)
        if M2 < 0:
            M2 = M2 % n
    else:
        print("b = ", b, ", C = ", intercepts[1][0])
        M2 = mod_pow(intercepts[1][0], b, n)
    M = (M1 * M2) % n
    print("Message = ", M)
else:
    print("Common Modulus Attack does not work with this intercepts.")

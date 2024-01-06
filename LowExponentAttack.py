def mod_inverse(mod, text, p=1, q=0, r=-1, count=0):
    new_p, new_q, new_r, modulus = q, p - (q * r), mod // text, mod % text
    if modulus == 1:
        return new_p - (new_q * new_r)
    else:
        return mod_inverse(text, modulus, new_p, new_q, new_r, count + 1)


def CRT(intercept):
    total = 0
    modulus = 1
    for i in intercept:
        prod = i[0]
        for j in intercept:
            if i[1] != j[1]:
                mod_value = (mod_inverse(i[1], j[1]))
                if mod_value < 0:
                    mod_value = mod_value % i[1]
                prod = prod * j[1] * mod_value
            else:
                continue
        total = total + prod
        modulus = modulus * i[1]
    return total % modulus, modulus


def find_root(degree, num):
    for nums in range(1, (num // degree) + 1):
        power = 1
        for deg in range(1, degree + 1):
            power = power * nums
        if power == num:
            return nums


# Should know e number of intercepts(C, n)
e = 3
intercepts = [[5, 7], [7, 11], [14, 31], [8, 45]]
# e = int(input("Enter e: "))
# intercepts = []
# for i in range(0, e):
#     print("Enter intercept ", i+1)
#     c = int(input("Enter C: "))
#     n = int(input("Enter n: "))
#     intercepts.append([c, n])
x, y = CRT(intercepts)
msg = find_root(e, x)
print("Message = ", x, " mod ", y)

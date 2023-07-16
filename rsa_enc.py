def rsa_enc(p, q, source_name):
    with open(source_name, "r", encoding="latin-1") as file:
        text = file.read()

    lk = []
    l1 = len(text)
    k10 = ""
    k20 = ""

    for i in range(0, l1):
        no = ord(text[i])
        n = p * q
        if no > n:
            print("Please enter correct text.........")
        else:
            t = (p - 1) * (q - 1)
            e = 0
            for i in range(2, t):
                if gcd(i, t) == 1:
                    e = i
                    break

            d = 0
            for i in range(1, 10):
                x = 1 + i * t
                if x % e == 0:
                    d = x // e
                    break

            ct = pow(no, e, n)
            lk.append(ct)
            ct1 = ct % 75
            print('n = ' + str(n) + ' e = ' + str(e) + ' t = ' + str(t) + ' d = ' + str(d) + ' cipher text = ' + str(ct1))
            k1 = chr(ct1)
            k10 = k10 + k1
            print("Cipher Value", k10)

    print("Original Value: ", lk)

    with open("sample1.txt", "w", encoding="latin-1") as file:
        file.write(k10)

    with open("sample2.txt", "w", encoding="latin-1") as file:
        for i in lk:
            file.write(str(i) + " ")

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

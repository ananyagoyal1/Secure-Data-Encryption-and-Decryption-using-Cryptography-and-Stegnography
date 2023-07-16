# rsa_dec.py
def rsa_dec(p, q, new_cover_name):
    with open("sample2.txt", "r", encoding="utf-8") as file:
     text = file.read()

    ct = list(map(int, s.split()))

    for i in range(len(ct)): 
        t = (p - 1) * (q - 1)
        for e in range(2, t):
            if gcd(e, t) == 1:
                break
        for j in range(1, 10):
            x = 1 + j * t 
            if (x % e == 0):
                d = int(x / e) 
                break
        dtt = pow(ct[i], d, n)
        dt = dtt % n
        print('n = ' + str(n) + ' e = ' + str(e) + ' t = ' + str(t) + ' d = ' + str(d) + ' decrypted text = ' + str(dt)) 
        k2 = chr(dt)
        k20 = k20 + k2
        print("Original Message: ", k20)

def gcd(a, b):
    if b == 0:
        return a 
    else:
        return gcd(b, a % b)

# stego_dec.py
from PIL import Image

def genData(data):
    # list of binary codes of given data
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def decode(cover_name):
    image = Image.open(cover_name, 'r')
    data = ''
    imgdata = iter(image.getdata())

    while True:
        pixels = [value for value in next(imgdata)[:3] + next(imgdata)[:3] + next(imgdata)[:3]]
        binstr = ''
        for i in pixels:
            if i % 2 == 0:
                binstr += '0'
            else:
                binstr += '1'
        data += chr(int(binstr, 2))
        if pixels[-1] % 2 != 0:
            k = data
            print(k)
            print(len(k))
            return data

def stego_dec(cover_name, new_cover_name):
    sq = decode(cover_name)
    print("Decoded word - " + sq)
    file = open(new_cover_name, "w")
    file.write(sq)
    file.close()

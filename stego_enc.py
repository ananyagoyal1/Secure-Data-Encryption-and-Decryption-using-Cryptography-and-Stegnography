# stego_enc.py
from PIL import Image

def genData(data):
    # list of binary codes
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
    for i in range(lendata):
        pix = [value for value in imdata.next()[:3] + imdata.next()[:3] + imdata.next()[:3]]
        for j in range(0, 8):
            if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                pix[j] -= 1
            elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                pix[j] -= 1
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]

def encode_enc(cover_img, data, new_img_name):
    new_img = cover_img.copy()
    w = new_img.size[0]
    (x, y) = (0, 0)
    for pixel in modPix(new_img.getdata(), data):
        new_img.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1
    new_img.save(new_img_name)

def stego_enc(cover_name, new_img_name, data):
    cover_img = Image.open(cover_name, 'r')
    encode_enc(cover_img, data, new_img_name)

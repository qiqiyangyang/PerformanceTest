#! /user/bin/env python
# encoding=utf-8
#__author__ ='zx'
#__time__ ='2017-10-1014:06'
'''
破解验证码
'''
from PIL import Image
import pytesseract
def recognize_captcha(imgpath):
    im = Image.open(imgpath).convert("L")
    # 1. threshold the image
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    out = im.point(table, '1')
    # out.show()
    # 2. recognize with tesseract
    num = pytesseract.image_to_string(out)
    return num

if __name__ == '__main__':
    res = recognize_captcha('securityCode.jpg')
    strs = res.split("\n")
    if len(strs) >=1:
        print (strs[0])

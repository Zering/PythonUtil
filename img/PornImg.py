#!/usr/bin/env python3
# encoding=utf-8
import sys
from PIL import Image

# http://blog.csdn.net/gzlaiyonghao/article/details/3166735
# 色情图片识别 py PornImg.py 图片文件

# 1. 转换为YCbCr色彩空间
img = Image.open(sys.argv[1]).convert('YCbCr')

w, h = img.size

data = img.getdata()

cnt = 0

for i, ycbcr in enumerate(data):

    y, cb, cr = ycbcr

    if 86 <= cb <= 117 and 140 <= cr <= 168:

        cnt += 1

print('%s %s a porn image.' % (sys.argv[1], 'is' if cnt > w * h * 0.3 else 'is not'))

import sys
import os
from json import loads

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

_, In, Out, Ans = sys.argv

ERR_OK = 0
ERR_WA = 1

maxpoints = 10

def compare(ans, out):
    x1 = cv2.imread(ans)
    x2 = cv2.imread(out)

    b1, g1, r1 = cv2.split(x1)
    b2, g2, r2 = cv2.split(x2)

    b = ssim(b1, b2)
    g = ssim(g1, g2)
    r = ssim(r1, r2)

    t = (b + g + r) / 3

    points = min(max(int(t * maxpoints), 0), maxpoints)
    print(points)
    print("ssim: {:06}".format(t))

    if t > 0.999:
        exit(ERR_OK)
    else:
        exit(ERR_WA)

compare(Ans, Out)

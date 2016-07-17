# coding:utf-8

import random
import matplotlib.pyplot as plt


def base_transformation(p, pxx, pxy, pyx, pyy, pyc):
    x = p[0]
    y = p[1]
    x1 = pxx*x + pxy*y
    y1 = pyx*x + pyy*y + pyc
    return x1, y1

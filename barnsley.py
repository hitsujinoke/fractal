# coding:utf-8


import random
import matplotlib.pyplot as plt


def base_transformation(p, pxx, pxy, pyx, pyy, pyc):
    x = p[0]
    y = p[1]
    x1 = pxx*x + pxy*y
    y1 = pyx*x + pyy*y + pyc
    return x1, y1


def transformation_(p):
    base_transformation(p, 0.85, 0.04, -0.04, 0.85)


def transformation_2(p):
    base_transformation(p, 0.2, -0.26, 0.23,)
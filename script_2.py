import math

c = 200


def volume(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    return a * b * c


def mass(a, b):
    a, b = int(a), int(b)
    return a * b * 18, 5


def sio(a, b):
    d = math.sqrt(a + b)
    return d

from script_2 import *
import time

v = input("value V:")

s = input("value S :")



for f in range(100):
    volume_ = volume(v, s, f)
    # time.sleep(1)
    print("for f  = {}  value = {}".format(f,volume_))


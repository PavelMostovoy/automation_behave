from script_2 import *
import time


def input_through_checker(inputdescription):
    while (True):
        try:
            entered_value = int(input(f"Enter a {inputdescription} "))
            break
        except ValueError:
            print("Invalid number")
    return int(entered_value)

v = input_through_checker("value numeric V:")

s = input_through_checker("velue numeric S")


for f in range(100):
    volume_ = volume(v, s, f)
    # time.sleep(1)
    print("for f  = {}  value = {}".format(f,volume_))


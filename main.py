import numpy as np
import matplotlib.pyplot as plt
from minimum_bounding_rectangle import minimum_bounding_rectangle as MBR
import random_mode
import manual_mode

def mode_picker():
    mode = input("Enter the mode(0 - is manual, 1 - is random, stop - to stop the program)\n").lower()
    match mode:
        case '0':
            print("Manual mode is selected")
            return manual_mode.run
        case '1':
            print("Random mode is selected")
            return random_mode.run
        case 'stop':
            return lambda: 'stop' 
        case _:
            print("Try again")
            mode_picker()

while True:
    runner = mode_picker()
    res = runner()
    if res == 'stop':
        break
    print("Points of the rectangle: " + str(res))
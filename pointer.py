from microbit import *

while True:
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    if abs(y) < 50 and abs(x) < 50:
        display.show("O")
    elif abs(y) > abs(x):
        if y > 50:
            display.show("D")
        elif y < -50:
            display.show("U")
    else:
        if x > 50:
            display.show("R")
        elif x < 50:
            display.show("L")
        

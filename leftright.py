from microbit import *

disp = 2
# Write your code here :-)
while True:
    if button_a.was_pressed():
        disp -= 1
    if button_b.was_pressed():
        disp += 1
    if disp == 5:
        disp -= 5
    if disp == -1:
        disp += 5
    display.clear()
    display.set_pixel(disp, 2, 9)
    sleep(10)
        

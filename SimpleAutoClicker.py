import keyboard
from pynput.mouse import Controller, Button
import time

stop = False
mouse = Controller()


def on_press():
    global stop
    stop = not stop
    print(stop)


keyboard.add_hotkey('f6', on_press)
while True:
    if stop:
        mouse.click(Button.left, 1)
    time.sleep(0.001)

import keyboard
from pynput.mouse import Controller, Button
import time

stop = False
mouse = Controller()


def on_press():
    global stop
    stop = not stop
    print(stop)


keyboard.add_hotkey('f6', on_press)  # < горячая клавиша для вкл/выкл кликера
while True:
    if stop:
        mouse.click(Button.left, 1)  # < Button.left / Button.right / Button.middle
    time.sleep(0.001)  # < задержка между кликами

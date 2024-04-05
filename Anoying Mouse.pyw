from pynput.mouse import Controller
import keyboard, random

mk = Controller()

random_number = 0

while True:
    if keyboard.is_pressed("n") and keyboard.is_pressed("m"):
        break
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    print(x,y)
    mk.move(x,y)


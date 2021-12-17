import time
import sys
# import keyboard
from pynput import keyboard


# Time delay parameters:
from ActionState import action_state

a = 2.5
b = 0.2
c = 0.08

# a = 0
# b = 0
# c = 0

class Writer():
    def __init__(self):
        pass

    def narrator(self, text):
        action_state["isNarrating"] = True
        print(text)
        time_to_wait = a
        if action_state["isSkipping"]:
            time_to_wait = 0
        time.sleep(a)


    def instruction(self, text):
        print(">>    " + text)
        time.sleep(b)


    def player(self, text):
        text = '"'+text+'"'
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        print()
        time.sleep(a)


    def NPC(self, name, text):
        text = '"'+text+'"'
        print(name+':', end =" ")
        for character in text:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        print()
        time.sleep(a)



if __name__ == "__main__":
    print("s")
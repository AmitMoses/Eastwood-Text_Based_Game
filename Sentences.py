import time
import sys



# Time delay parameters:
a = 3
a1 = 0.5
b = 0.2
c = 0.08

# a = 0
# b = 0
# c = 0
# a1 = 0


def narrator(text):
    print(text)
    time.sleep(a)


def instruction(text):
    print(">>    " + text)
    time.sleep(b)


def player(text):
    text = '"'+text+'"'
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a1)


def NPC(name, text):
    text = '"'+text+'"'
    print(name+':', end=" ")
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a1)


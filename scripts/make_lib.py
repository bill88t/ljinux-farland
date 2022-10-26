from platform import uname
from os import listdir, system


def errexit():
    print("Compilation error, exiting")
    exit(1)


mpyn = "./scripts/mpy-cross-" + uname().machine

print(f"Compiling adafruit_framebuf..\nUsing mpycross: {mpyn}\n")

a = system(
    mpyn
    + " ./submodules/Adafruit_CircuitPython_framebuf/adafruit_framebuf.py -s adafruit_framebuf -v -O4 -o ./files/adafruit_framebuf.mpy"
)
print("adafruit_framebuf.py -> adafruit_framebuf.mpy")

if a != 0:
    errexit()

print()

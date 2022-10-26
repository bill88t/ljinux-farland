opts = ljinux.api.xarg()
li = opts["hw"] + opts["w"]
del opts  # no opts needed, just words
farland_prefix = f"{colors.red_t}Farland{colors.endc}: "
help_t = """Ljinux farland

Usage:
    farland setup [scl] [sda] [optional: width] [optional: height]
    farland pixel [x] [y] [color]
    farland line [xstart] [ystart] [xend] [yend] [color]
    farland circle [xcenter] [ycenter] [radius] [color]
    farland filled_circle [xcenter] [ycenter] [radius] [color]
    farland triangle [x1] [y1] [x2] [y2] [x3] [y3] [color]
    farland filled_triangle [x1] [y1] [x2] [y2] [x3] [y3] [color]
    farland text [x] [y] [text] [color]
    farland fill [color]
"""

if len(li) > 0 and li[0] == "setup":
    if "display" in ljinux.modules:
        # Prepare args
        for pin in [int(li[1]), int(li[2])]:
            if pin not in pintab:
                del pin
                raise Exception("Pin unknown")
            elif pin in pin_alloc:
                del pin
                raise Exception("Pin in use")
            pin_alloc.add(pin)
            del pin

        x = 128 if len(li) < 4 else li[3]
        y = 64 if len(li) < 5 else li[4]
        # Setup
        ljinux.modules["display"].setup(pintab[int(li[1])], pintab[int(li[2])], x, y)
        del x, y
    else:
        print(farland_prefix + "No display kernel module loaded.")
elif "display" in ljinux.modules and ljinux.modules["display"].connected:
    if len(li) > 0:
        if li[0] == "pixel":
            if len(li) is 4:
                ljinux.modules["display"].pixel(
                    int(li[1]), int(li[2]), int(li[3])
                )  # x, y, col
            else:
                print(
                    farland_prefix
                    + "Position and color arguments required.\n"
                    + 'Example: "farland pixel 10 20 1", draws a pixel in [10, 20] with color 1.'
                )
        elif li[0] == "line":
            if len(li) is 6:
                ljinux.modules["display"].line(
                    int(li[1]), int(li[2]), int(li[3]), int(li[4]), int(li[5])
                )
                # xstart, ystart, xend, yend, col
            else:
                print(
                    farland_prefix
                    + "Start position, end position and color arguments required.\n"
                    + 'Example: "farland line 10 20 30 40 1"\n'
                    + "Which draws a line from [10, 20] to [30, 40] with color 1."
                )
        elif li[0] == "circle":
            if len(li) is 5:
                ljinux.modules["display"].circle(
                    int(li[1]), int(li[2]), int(li[3]), int(li[4])
                )
                # xcenter, ycenter, radius, col
            else:
                print(
                    farland_prefix
                    + "Center position, radius and color arguments required.\n"
                    + 'Example: "farland circle 10 20 5 1"\n'
                    + "Which draws a circle with center [10, 20] with radius 5 and color 1."
                )
        elif li[0] == "filled_circle":
            if len(li) is 5:
                ljinux.modules["display"].circle(
                    int(li[1]), int(li[2]), int(li[3]), int(li[4]), fill=True
                )
                # xcenter, ycenter, radius, col
            else:
                print(
                    farland_prefix
                    + "Center position, radius and color arguments required.\n"
                    + 'Example: "farland filled_circle 10 20 5 1"\n'
                    + "Which draws a filled circle with center [10, 20] with radius 5 and color 1."
                )
        elif li[0] == "triangle":
            if len(li) is 8:
                ljinux.modules["display"].triangle(
                    int(li[1]),
                    int(li[2]),
                    int(li[3]),
                    int(li[4]),
                    int(li[5]),
                    int(li[6]),
                    int(li[7]),
                )
                # x1, y1, x2, y2, x3, y3, col
            else:
                print(
                    farland_prefix
                    + "3 point positions and color arguments required.\n"
                    + 'Example: "farland triangle 1 1 5 5 12 20 1"\n'
                    + "Which draws a triangle with points [1, 1], [5, 5], [12, 20] and color 1."
                )
        elif li[0] == "filled_triangle":
            if len(li) is 8:
                ljinux.modules["display"].triangle(
                    int(li[1]),
                    int(li[2]),
                    int(li[3]),
                    int(li[4]),
                    int(li[5]),
                    int(li[6]),
                    int(li[7]),
                    fill=True,
                )
                # x1, y1, x2, y2, x3, y3, col
            else:
                print(
                    farland_prefix
                    + "3 point positions and color arguments required.\n"
                    + 'Example: "farland filled_triangle 1 1 5 5 12 20 1"\n'
                    + "Which draws a filled triangle with points [1, 1], [5, 5], [12, 20] and color 1."
                )
        elif li[0] == "square":
            pass
        elif li[0] == "filled_square":
            pass
        elif li[0] == "text":
            if len(li) is 5:
                ljinux.modules["display"].text(
                    int(li[1]), int(li[2]), li[3], int(li[4])
                )
                # x, y, text, col
            else:
                print(
                    farland_prefix
                    + "Position, text and color arguments required.\n"
                    + 'Example: "farland text 1 1 amogus 1"\n'
                    + "Which writes amogus from [1, 1] with color 1."
                )
        elif li[0] == "fill":
            if len(li) is 2:
                ljinux.modules["display"].fill(int(li[1]))
            else:
                print(
                    farland_prefix
                    + "Color argument required.\n"
                    + 'Example: "farland fill 1"\n'
                    + "Fills the display with color 1."
                )
        else:
            print(help_t)
    else:
        print(help_t)
else:
    if len(li) is 0:
        print(help_t)
    ljinux.based.error(6, prefix=f"{colors.red_t}Farland{colors.endc}")

del li, farland_prefix, help_t

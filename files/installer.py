for filee in ["farland.lja", "farland.py"]:
    ljinux.api.setvar("argj", f"cp {filee} /bin/{filee}")
    ljinux.based.command.fpexec("/bin/cp.py")

ljinux.api.setvar("argj", "cp font5x8.bin /etc/font5x8.bin")
ljinux.based.command.fpexec("/bin/cp.py")

ljinux.api.setvar("argj", "cp adafruit_framebuf.mpy &/lib/adafruit_framebuf.mpy")
ljinux.based.command.fpexec("/bin/cp.py")

ljinux.api.setvar("return", "0")

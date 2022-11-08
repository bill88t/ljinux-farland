for filee in ["farland.lja", "farland.py"]:
    ljinux.api.setvar("argj", "rm /bin/" + filee)
    ljinux.based.command.fpexec("/bin/rm.py")

ljinux.api.setvar("argj", "rm /etc/font5x8.bin")
ljinux.based.command.fpexec("/bin/rm.py")

ljinux.api.setvar("argj", "rm &/lib/adafruit_framebuf.mpy")
ljinux.based.command.fpexec("/bin/rm.py")

ljinux.api.setvar("return", "0")

for filee in ["farland.lja", "farland.py"]:
    ljinux.api.var("argj", "rm /bin/" + filee)
    ljinux.based.command.fpexecc([None, "/bin/rm.py"])

ljinux.api.var("argj", "rm /etc/font5x8.bin")
ljinux.based.command.fpexecc([None, "/bin/rm.py"])

ljinux.api.var("argj", "rm &/lib/adafruit_framebuf.mpy")
ljinux.based.command.fpexecc([None, "/bin/rm.py"])

ljinux.api.var("return", "0")

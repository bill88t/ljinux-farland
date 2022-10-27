for filee in ["farland.lja", "farland.py"]:
    ljinux.api.var("argj", f"cp {filee} /bin/{filee}")
    ljinux.based.command.fpexecc([None, "/bin/cp.py"])

ljinux.api.var("argj", "cp font5x8.bin /etc/font5x8.bin")
ljinux.based.command.fpexecc([None, "/bin/cp.py"])

ljinux.api.var("argj", "cp adafruit_framebuf.mpy &/lib/adafruit_framebuf.mpy")
ljinux.based.command.fpexecc([None, "/bin/cp.py"])

ljinux.api.var("return", "0")

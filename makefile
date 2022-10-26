SHELL = bash
all:
	@echo -e "Ljinux farland builder.\n\nUsage:\n\tmake package\n\tmake clean"
update_modules:
	@echo "Updating git submodules from remotes.."
	@git submodule update --init --recursive --remote .
	@echo -e "Submodules ready\n\nMake sure to git commit before procceding to make!!"
modules:
	@echo "Preparing git submodules.."
	@git submodule update --init --recursive .
	@echo "Submodules ready"
package: modules
	@python3 -u scripts/make_lib.py
	@python3 -u scripts/generate_package.py
clean:
	@if [ -e "farland.jpk" ]; then rm farland.jpk; fi
	@if [ -e "./files/adafruit_framebuf.mpy" ]; then rm ./files/adafruit_framebuf.mpy; fi

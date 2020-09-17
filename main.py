from pystray import MenuItem as item
import pystray
import pyperclip
from PIL import Image

def scrub(icon):
	pyperclip.copy("")

def exit(icon):
	icon.stop()

def main():
	image = Image.open("icon.png")

	menu = pystray.Menu(
		item('Clipboard Scrubber', scrub, default=True, enabled=False),
		pystray.Menu.SEPARATOR, item('Exit', exit))
	icon = pystray.Icon('clipboardscrubber', image, 'Clipboard Scrubber', menu)
	icon.run()

if __name__ == "__main__":
	main()
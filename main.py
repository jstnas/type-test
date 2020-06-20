import os
import colorama
from colorama import Fore, Back, Style
from pynput import keyboard


class App:
	def __init__(self):
		colorama.init()
		self.text = ""
		self.input = ""

	@staticmethod
	def clear():
		os.system('cls' if os.name == 'nt' else 'clear')

	def set_text(self, new_text: str):
		self.text = new_text

	def print_prompt(self):
		self.clear()
		output = ""
		# Check for completion.
		if len(self.input) >= len(self.text):
			return True
		# Go through each character in the text.
		for i in range(len(self.text)):
			colour = Fore.WHITE
			char = self.text[i]
			# Set foreground colour.
			if len(self.input) <= i:
				colour = Fore.LIGHTBLACK_EX
			elif self.input[i] != self.text[i]:
				colour = Fore.RED
				#char = self.input[i]

			output += f"{colour}{char}{Style.RESET_ALL}"
			#output += colour
			#output += char
			#output += Style.RESET_ALL
		print(output, end="", flush=True)

	def on_press(self, key: keyboard.Key):
		try:
			self.input += key.char
		except AttributeError:
			if key == keyboard.Key.esc:
				return False
			elif key == keyboard.Key.space:
				self.input += " "
			elif key == keyboard.Key.backspace:
				self.input = self.input[:-1]
			elif key == keyboard.Key.enter:
				self.input += "\n"
		finally:
			result = self.print_prompt()
			if result:
				return False

	def start(self, text: str):
		self.text = text
		self.print_prompt()
		with keyboard.Listener(on_press=self.on_press) as listener:
			listener.join()
		print("Completed")

if __name__ == '__main__':
	app = App()
	app.start("The quick brown fox jumps over the lazy fox!\nand then he jumps some more.")

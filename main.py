import os
import colorama
from colorama import Fore, Back, Style
from pynput import keyboard


class App:
    def __init__(self):
        colorama.init()
        self.text = ""
        self.input = ""
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def set_text(self, new_text: str):
        self.text = new_text

    def print_prompt(self):
        output = ""
        length = len(self.text) if len(self.text) > len(self.input) else len(self.input)
        colour = Fore.WHITE
        for i in range(length):
            # Set foreground colour.
            if len(self.input) <= i:
                colour = Fore.LIGHTBLACK_EX
            elif self.input[i] != self.text[i]:
                colour = Fore.RED
            output += colour

            output += self.text[i]
            output += Style.RESET_ALL
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

    def main_loop(self):
        try:
            while True:
                self.clear()
                self.print_prompt()
        except Exception as e:
            print(e)
            return


if __name__ == '__main__':
    app = App()
    app.set_text("The quick brown fox jumps over the lazy fox!\nand then he jumps some more.")
    app.main_loop()

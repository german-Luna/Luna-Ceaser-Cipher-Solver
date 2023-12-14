from collections import deque
import keyboard
import os
import time
from platform import system

def clear_screen():
    """Clear the console screen."""
    if system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def shift_characters(char_deque, direction):
    """Shift characters in the given direction."""
    if direction == "right":
        char_deque.rotate(1)
    elif direction == "left":
        char_deque.rotate(-1)

def print_characters(char_deque):
    """Print characters in the deque."""
    clear_screen()
    print(''.join(map(str, char_deque)))

def main():
    print("Press CRTL + C to exit")
    input_string = input("What are you trying to solve: ")
    char_deque = deque(list(input_string))

    prev_d_pressed = False
    prev_a_pressed = False

    try:
        while True:
            d_pressed = keyboard.is_pressed("d")
            a_pressed = keyboard.is_pressed("a")

            if d_pressed and not prev_d_pressed:
                shift_characters(char_deque, "right")
                print_characters(char_deque)

            elif a_pressed and not prev_a_pressed:
                shift_characters(char_deque, "left")
                print_characters(char_deque)

            prev_d_pressed = d_pressed
            prev_a_pressed = a_pressed

            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()

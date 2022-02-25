import os

from pynput import keyboard


def close_app():
    os.abort()


def initialize_keyboard_hotkeys():
    with keyboard.GlobalHotKeys({'<alt>+1': close_app}) as h:
        h.join()

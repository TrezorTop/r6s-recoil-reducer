import os

from pynput import keyboard
from pynput.keyboard import Key

from core.app_state import app_state
from core.screen_reader.screen_reader import determine_profile


def close_app():
    os.abort()


def pause():
    app_state.set_paused(not app_state.is_paused())


def set_profile_1():
    app_state.set_forces([0, 68])


def set_profile_2():
    app_state.set_forces([0, 32])


def set_profile_3():
    app_state.set_forces([0, 17])


def initialize_keyboard_hotkeys():
    with keyboard.GlobalHotKeys(
            {
                '<ctrl>+1': pause,

                'm+0': close_app,
                '<alt>+1': set_profile_1,
                '<alt>+2': set_profile_2,
                '<alt>+3': set_profile_3
            }) as h:
        h.join()


def on_press(key):
    if key == Key.f1:
        set_profile_1()
    if key == Key.f2:
        set_profile_2()
    if key == Key.f3:
        set_profile_3()
    if key == Key.f5:
        determine_profile()


keyboard_listener = keyboard.Listener(on_press=on_press)

set_profile_1()

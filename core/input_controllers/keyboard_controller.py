import os

from pynput import keyboard

from core.app_state import app_state


def close_app():
    os.abort()


def pause():
    app_state.set_paused(not app_state.is_paused())


def set_profile_1():
    app_state.x_force = 0
    app_state.y_force = 16


def set_profile_2():
    app_state.x_force = 0
    app_state.y_force = 27


def set_profile_3():
    app_state.x_force = 0
    app_state.y_force = 15


def initialize_keyboard_hotkeys():
    with keyboard.GlobalHotKeys(
            {
                '<alt>+0': close_app,
                '<ctrl>+1': pause,
                '<alt>+1': set_profile_1,
                '<alt>+2': set_profile_2,
                '<alt>+3': set_profile_3
            }) as h:
        h.join()


set_profile_1()

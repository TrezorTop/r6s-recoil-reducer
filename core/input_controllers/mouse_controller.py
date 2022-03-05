import threading
import time

from pynput import mouse
from pynput.mouse import Listener as MouseListener

from core.app_state import app_state, mouse_state
from core.screen_reader.screen_reader import determine_profile
from utils.mouse_control import control_mouse


def on_click(x, y, button, pressed):
    if button == mouse.Button.x1:
        if pressed:
            determine_profile()

    app_state.set_forces_delay_state([True, False])

    if app_state.is_paused():
        return

    if button == mouse.Button.right:
        if pressed:
            if not mouse_state.is_right_button_pressed():
                mouse_state.set_right_button_pressed(True)
        else:
            mouse_state.set_right_button_pressed(False)

    if button == mouse.Button.left:
        if pressed and mouse_state.is_right_button_pressed():
            if not app_state.is_running():
                app_state.set_running(True)
                threading.Thread(target=process).start()
                threading.Thread(
                    target=delay,
                    args=[app_state.get_forces_delay()['x'], app_state.get_forces_delay()['y']]
                ).start()
        else:
            app_state.set_running(False)


def process():
    while app_state.is_running():
        threading.Thread(target=control_mouse).start()
        time.sleep(0.01)


def delay(x_delay, y_delay):
    time.sleep(x_delay)
    app_state.set_forces_delay_state([False, False])


mouse_listener = MouseListener(on_click=on_click)

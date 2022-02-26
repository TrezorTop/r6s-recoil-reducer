import threading
import time

from pynput import mouse
from pynput.mouse import Listener as MouseListener

from core.app_state import app_state, mouse_state
from utils.mouse_move import mousemove


def on_click(x, y, button, pressed):
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
        else:
            app_state.set_running(False)


def process():
    while app_state.is_running():
        threading.Thread(target=mousemove, args=[app_state.get_forces()['x'], app_state.get_forces()['y']]).start()
        time.sleep(0.01)


mouse_listener = MouseListener(on_click=on_click)

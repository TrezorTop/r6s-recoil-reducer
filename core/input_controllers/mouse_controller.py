import threading
import time

from pynput import mouse
from pynput.mouse import Listener as MouseListener

from core.app_state import app_state
from utils.mouse_move import mousemove


def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            if not app_state.is_running() and not app_state.is_paused():
                app_state.set_running(True)
                threading.Thread(target=process).start()
        else:
            app_state.set_running(False)


def process():
    while app_state.is_running():
        threading.Thread(target=mousemove, args=[0, 25]).start()
        time.sleep(0.01)


mouse_listener = MouseListener(on_click=on_click)

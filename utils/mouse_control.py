import win32api
import win32con
from pynput.mouse import Controller

from core.app_state import app_state

mouse_controller = Controller()


def control_mouse():
    if app_state.get_auto_click():
        mouse_click()

    mouse_move(app_state.get_forces()['x'], app_state.get_forces()['y'])


def mouse_move(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x), int(y), 0, 0)


def mouse_click():
    pass
    # win32api.keybd_event(0x77, 0, 0)

    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

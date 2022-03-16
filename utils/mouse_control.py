import win32api
import win32con
from pynput.mouse import Controller

from core.app_state import app_state

mouse_controller = Controller()


def control_mouse():
    mouse_move(app_state.get_forces()['x'], app_state.get_forces()['y'])


def mouse_move(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x), int(y), 0, 0)

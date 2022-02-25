from core.input_controllers.keyboard_controller import initialize_keyboard_hotkeys
from core.input_controllers.mouse_controller import mouse_listener

mouse_listener.start()

initialize_keyboard_hotkeys()

mouse_listener.join()

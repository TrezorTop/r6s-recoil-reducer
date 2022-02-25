class AppState:
    __running = False
    __paused = False

    def set_running(self, state):
        self.__running = state

    def set_paused(self, state):
        self.__paused = state

    def is_running(self):
        return self.__running

    def is_paused(self):
        return self.__paused

    x_force = 0
    y_force = 0


class MouseState:
    __right_button_pressed = False

    def set_right_button_pressed(self, state):
        self.__right_button_pressed = state

    def is_right_button_pressed(self):
        return self.__right_button_pressed


app_state = AppState()
mouse_state = MouseState()

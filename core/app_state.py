class AppState:
    __running = False
    __paused = False

    __x_force = 0
    __y_force = 0

    def set_running(self, state):
        self.__running = state

    def set_paused(self, state):
        self.__paused = state

        print("paused:", self.is_paused())

    def is_running(self):
        return self.__running

    def is_paused(self):
        return self.__paused

    def set_forces(self, x, y):
        self.__x_force = x
        self.__y_force = y

        print("forces:", [x, y])

    def get_forces(self):
        d = dict()
        d['x'] = self.__x_force
        d['y'] = self.__y_force

        return d


class MouseState:
    __right_button_pressed = False

    def set_right_button_pressed(self, state):
        self.__right_button_pressed = state

    def is_right_button_pressed(self):
        return self.__right_button_pressed


app_state = AppState()
mouse_state = MouseState()

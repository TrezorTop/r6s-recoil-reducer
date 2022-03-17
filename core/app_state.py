from core.json_reader.json_reader import get_in_game_mouse_sensitivity


class AppState:
    __running = False
    __paused = False

    __auto_click = False

    __x_force = 0
    __y_force = 0

    __x_force_delay = 0
    __y_force_delay = 0

    __x_force_delayed = True
    __y_force_delayed = False

    def set_auto_click(self, state):
        self.__auto_click = state

    def get_auto_click(self):
        return self.__auto_click

    def set_running(self, state):
        self.__running = state

    def set_paused(self, state):
        self.__paused = state

        print("paused:", self.is_paused())

    def is_running(self):
        return self.__running

    def is_paused(self):
        return self.__paused

    def set_forces(self, array):
        self.__x_force = int(array[0] / app_data.get_in_game_mouse_sensitivity())
        self.__y_force = int(array[1] / app_data.get_in_game_mouse_sensitivity())

        self.__x_force_delay = array[2]
        self.__y_force_delay = array[3]

        print("forces:", array)

    def get_forces(self):
        d = dict()

        d['x'] = 0 if self.__x_force_delayed else self.__x_force
        d['y'] = 0 if self.__y_force_delayed else self.__y_force

        return d

    def set_forces_delay(self, array):
        self.__x_force_delay = array[0]
        self.__y_force_delay = array[1]

        print("forces delay:", array)

    def set_forces_delay_state(self, array):
        self.__x_force_delayed = array[0]
        self.__y_force_delayed = array[1]

    def get_forces_delay(self):
        d = dict()
        d['x'] = self.__x_force_delay
        d['y'] = self.__y_force_delay

        return d


class AppData:
    __profile_list = []
    __in_game_mouse_sensitivity = 1

    def get_in_game_mouse_sensitivity(self):
        return self.__in_game_mouse_sensitivity

    def set_in_game_mouse_sensitivity(self, value):
        self.__in_game_mouse_sensitivity = value

    def set_profile_list(self, profile_list):
        self.__profile_list = profile_list

    def get_profile_list(self):
        return self.__profile_list


class MouseState:
    __right_button_pressed = False

    def set_right_button_pressed(self, state):
        self.__right_button_pressed = state

    def is_right_button_pressed(self):
        return self.__right_button_pressed


app_state = AppState()
app_data = AppData()
mouse_state = MouseState()
app_data.set_in_game_mouse_sensitivity(int(get_in_game_mouse_sensitivity()))

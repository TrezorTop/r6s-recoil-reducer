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


app_state = AppState()

from python_imagesearch.imagesearch import imagesearcharea

from core.app_state import app_data, app_state
from core.json_reader.json_reader import get_profile_list, get_profile


def determine_profile():
    app_data.set_profile_list(get_profile_list())

    screen = app_state.get_screen_rectangle()

    for key in [element for element in app_data.get_profile_list() if
                element not in {'profile_1', 'profile_2', 'profile_3', 'default'}]:
        try:
            res = imagesearcharea(
                './settings/icons_to_search/' + key + '.png',
                screen['x0'],
                screen['y0'],
                screen['x1'],
                screen['y1'],
                0.9,
                screen['region']
            )

            if res[0] != -1:
                app_state.set_forces(get_profile(key))
                return
        except FileNotFoundError:
            print('[WARNING]:', key, 'image not found')

    print("nothing found, setting default")
    app_state.set_forces(get_profile("default"))

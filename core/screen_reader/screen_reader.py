import ctypes

from python_imagesearch.imagesearch import imagesearch_from_folder

from core.app_state import app_data, app_state
from core.json_reader.json_reader import get_in_game_mouse_sensitivity, get_profile_list, get_profile


def determine_profile():
    app_data.set_profile_list(get_profile_list())

    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    x0 = int(screensize[0] - screensize[0] / 3)
    y0 = int(screensize[1] - screensize[1] / 3)
    x1 = int(screensize[0])
    y1 = int(screensize[1])

    results = dict(imagesearch_from_folder('./settings/icons_to_search/', 1.2))

    for key in results:
        if results[key][0] > -1:
            for i in app_data.get_profile_list():
                if str(key).find(i) > -1:
                    app_state.set_forces(get_profile(i))
                    return
    app_state.set_forces(get_profile("profile_1"))

import json


def get_profile(key):
    with open('./settings/settings.json') as json_file:
        print("Profile:", key)
        data = json.load(json_file)

        return [
            data['profiles'][key]['x'],
            data['profiles'][key]['y'],
            data['profiles'][key]['x_delay'],
            data['profiles'][key]['y_delay'],
            data['profiles'][key]['auto_click']
        ]


def get_in_game_mouse_sensitivity():
    with open('./settings/settings.json') as json_file:
        data = json.load(json_file)

        return data['settings']['in_game_mouse_sensitivity']


def get_profile_list():
    with open('./settings/settings.json') as json_file:
        data = json.load(json_file)

        return [*dict(data['profiles'])]

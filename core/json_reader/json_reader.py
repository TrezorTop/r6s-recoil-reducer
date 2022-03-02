import json


def get_profile(key):
    with open('./settings/settings.json') as json_file:
        data = json.load(json_file)

        return [data['profiles'][key]['x'], data['profiles'][key]['y']]


def get_in_game_mouse_sensitivity():
    with open('./settings/settings.json') as json_file:
        data = json.load(json_file)

        return data['settings']['in_game_mouse_sensitivity']


def get_profile_list():
    with open('./settings/settings.json') as json_file:
        data = json.load(json_file)

        return [*dict(data['profiles'])]

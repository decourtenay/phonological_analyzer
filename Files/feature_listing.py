#  Not executable directly

from importer import sound_importer
sounds = sound_importer('sounds.csv')


def feature_listing():
    value_list = []
    feature_list = []
    for sound in sounds:
        for value in sound.values():
            if value not in value_list:
                # if len(value) > 2:
                value_list.append(value)
    for sound in sounds:
        for feature in sound.keys():
            if feature not in feature_list:
                feature_list.append(feature)
    return value_list, feature_list, sounds


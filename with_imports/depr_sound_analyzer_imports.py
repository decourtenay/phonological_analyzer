from importer import sound_importer


def sound_class_finder(sound_class):
    sound_class_list = []
    for sound in sounds:
        if sound['place'] == sound_class or sound['manner'] == sound_class or sound['voicing'] == sound_class\
                or sound['type'] == sound_class or sound['height'] == sound_class or sound['backness'] == sound_class\
                or sound['roundness'] == sound_class:
            sound_class_list.append(sound['symbol'])
    print(f"The sounds with the feature \"{sound_class}\" are {sound_class_list}")

sounds = sound_importer('sounds.csv')
sound_class_finder('rounded')

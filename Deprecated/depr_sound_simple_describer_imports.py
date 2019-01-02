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
    return value_list, feature_list


def simple_describer():
    value_list, feature_list = feature_listing()
    for feature in feature_list:
        for value in value_list:
            individual_value = []
            for sound in sounds:
                if sound[feature] == value:
                    individual_value.append(sound['symbol'])
            if individual_value and value:
                print(f"The sounds with the feature \"{value}\" are {individual_value}")


def sound_feature_analyzer(feature):
    value_list, feature_list = feature_listing()
    for value in value_list:
        individual_value = []
        for sound in sounds:
            if sound[feature] == value:
                individual_value.append(sound['symbol'])
        if individual_value and value:
            print(f"The sounds with the feature \"{value}\" are {individual_value}")


def sound_feature_value_analyzer(value):
    value_list, feature_list = feature_listing()
    for feature in feature_list:
        individual_value = []
        for sound in sounds:
            if sound[feature] == value:
                individual_value.append(sound['symbol'])
        if individual_value and value:
            print(f"The sounds with the feature \"{value}\" are {individual_value}")


def sound_feature_value_analyzer_2(value1, value2):
    value_list, feature_list = feature_listing()
    for feature1 in feature_list:
        individual_value = []
        for sound in sounds:
            if sound[feature1] == value1:
                for feature2 in feature_list:
                    if sound[feature2] == value2:
                        individual_value.append(sound['symbol'])
        if individual_value and value1 and value2:
            print(f"The sounds with the feature combination \"{value1}\" and \"{value2}\" are {individual_value}")

sounds = sound_importer('sounds.csv')
feature_listing()
# simple_describer()
sound_feature_analyzer('place')
sound_feature_value_analyzer('alveolar')
sound_feature_value_analyzer_2('dental', 'stop')


from feature_listing import feature_listing


def feature_combination_analyzer(value1, value2):
    value_list, feature_list, sounds = feature_listing()
    individual_value = []
    for feature1 in feature_list:
        for sound in sounds:
            if sound[feature1] == value1:
                for feature2 in feature_list:
                    if sound[feature2] == value2:
                        individual_value.append(sound['symbol'])
    if individual_value:
        print(f"The sounds with the feature value combination \"{value1}\" and \"{value2}\" are {individual_value}")
    else:
        print(f"There are no sounds that are both \"{value1}\" and \"{value2}\"")


feature_combination_analyzer('high', 'low')
feature_combination_analyzer('low', 'central')
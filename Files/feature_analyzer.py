from feature_listing import feature_listing


def feature_analyzer(feature):
    value_list, feature_list, sounds = feature_listing()
    for value in value_list:
        individual_value = []
        for sound in sounds:
            if sound[feature] == value:
                individual_value.append(sound['symbol'])
        if individual_value and value:
            print(f"The sounds for which the value of the feature \"{feature}\" is \"{value}\" are {individual_value}")


feature_analyzer('voicing')
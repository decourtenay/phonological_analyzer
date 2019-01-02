from feature_listing import feature_listing


def natural_class_describer():
    value_list, feature_list, sounds = feature_listing()
    for feature in feature_list:
        for value in value_list:
            individual_value = []
            for sound in sounds:
                if sound[feature] == value:
                    individual_value.append(sound['symbol'])
            if individual_value and value:
                print(f"The sounds with the feature value \"{value}\" are {individual_value}")


natural_class_describer()
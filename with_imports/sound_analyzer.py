from feature_listing import feature_listing


def sound_analyzer(analyzed_sound):
    value_list, feature_list, sounds = feature_listing()
    feature_values = []
    for sound in sounds:
        if sound['symbol'] == analyzed_sound:
            for feature in feature_list:
                if len(sound[feature]) >= 2:
                    feature_values.append(sound[feature])
    print(f"The feature values of the sound \"{analyzed_sound}\" are {feature_values}")


sound_analyzer('t')
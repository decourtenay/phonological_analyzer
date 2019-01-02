from feature_listing import feature_listing


def sound_set_analyzer(analyzed_sound1, analyzed_sound2):
    value_list, feature_list, sounds = feature_listing()
    feature_values = []
    for sound1 in sounds:
        if sound1['symbol'] == analyzed_sound1:
            for sound2 in sounds:
                if sound2['symbol'] == analyzed_sound2:
                    for feature in feature_list:
                        if sound1[feature] == sound2[feature]:
                            if len(sound1[feature]) >= 2:
                                feature_values.append(sound1[feature])
    if not feature_values:
        print(f"The sounds \"{analyzed_sound1}\" and \"{analyzed_sound2}\" do not share any feature values")
    else:
        print(f"The sounds \"{analyzed_sound1}\" and \"{analyzed_sound2}\" share the following feature values:"
              f" {feature_values}")


sound_set_analyzer('m', 'f')
sound_set_analyzer('sh', 'f')
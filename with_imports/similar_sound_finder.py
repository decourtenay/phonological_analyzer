from feature_listing import feature_listing


def similar_sound_finder(analyzed_sound):
    value_list, feature_list, sounds = feature_listing()
    for sound1 in sounds:
        if sound1['symbol'] == analyzed_sound:
            for feature in feature_list:
                shared_feature_list = []
                for sound2 in sounds:
                    if sound1[feature] == sound2[feature]:
                        if sound1['symbol'] != sound2['symbol']:
                            shared_feature_list.append(sound2['symbol'])
                if len(shared_feature_list) > 1:
                    if sound1[feature]:
                        print(f"The sound \"{analyzed_sound}\" shares the feature value \"{sound1[feature]}\" with"
                              f" {shared_feature_list}")


similar_sound_finder('k')
similar_sound_finder('u')

from importer import sound_importer


def sound_unpacker():

    global consonants
    consonants = {}
    global vowels
    vowels = {}

    global voiceless
    voiceless = {}
    global voiced
    voiced = {}

    global labials
    labials = {}
    global dentals
    dentals = {}
    global alveolars
    alveolars = {}
    global palatals
    palatals = {}
    global retroflexes
    retroflexes = {}
    global velars
    velars = {}

    global stops
    stops = {}
    global fricatives
    fricatives = {}
    global affricates
    affricates = {}
    global nasals
    nasals = {}
    global approximants
    approximants = {}
    global laterals
    laterals = {}

    global front_vowels
    front_vowels = {}
    global central_vowels
    central_vowels = {}
    global back_vowels
    back_vowels = {}

    global high_vowels
    high_vowels = {}
    global mid_vowels
    mid_vowels = {}
    global low_vowels
    low_vowels = {}

    global rounded_sounds
    rounded_sounds = {}
    global unrounded_sounds
    unrounded_sounds = {}

    for sound in sounds:
        if sound['type'] == 'consonant':
            consonants[sound['symbol']] = sound
        else:
            vowels[sound['symbol']] = sound

    for sound in sounds:
        if sound['voicing'] == 'voiceless':
            voiceless[sound['symbol']] = sound
        else:
            voiced[sound['symbol']] = sound

    for sound in sounds:
        if sound['type'] == 'consonant':
            if sound['place'] == 'labial':
                labials[sound['symbol']] = sound
            elif sound['place'] == 'dental':
                dentals[sound['symbol']] = sound
            elif sound['place'] == 'alveolar':
                alveolars[sound['symbol']] = sound
            elif sound['place'] == 'palatal':
                palatals[sound['symbol']] = sound
            elif sound['place'] == 'retroflex':
                retroflexes[sound['symbol']] = sound
            elif sound['place'] == 'velar':
                velars[sound['symbol']] = sound
        elif sound['type'] == 'vowel':
            if sound['backness'] == 'front':
                front_vowels[sound['symbol']] = sound
            elif sound['backness'] == 'central':
                central_vowels[sound['symbol']] = sound
            elif sound['backness'] == 'back':
                back_vowels[sound['symbol']] = sound

    for sound in sounds:
        if sound['type'] == 'consonant':
            if sound['manner'] == 'stop':
                stops[sound['symbol']] = sound
            elif sound['manner'] == 'fricative':
                fricatives[sound['symbol']] = sound
            elif sound['manner'] == 'affricate':
                affricates[sound['symbol']] = sound
            elif sound['manner'] == 'nasal':
                nasals[sound['symbol']] = sound
            elif sound['manner'] == 'approximant':
                approximants[sound['symbol']] = sound
            elif sound['manner'] == 'lateral':
                laterals[sound['symbol']] = sound
        elif sound['type'] == 'vowel':
            if sound['height'] == 'high':
                high_vowels[sound['symbol']] = sound
            elif sound['height'] == 'mid':
                mid_vowels[sound['symbol']] = sound
            elif sound['height'] == 'low':
                low_vowels[sound['symbol']] = sound

    for sound in sounds:
        if sound['roundness'] == 'rounded':
            rounded_sounds[sound['symbol']] = sound
        else:
            unrounded_sounds[sound['symbol']] = sound


def sound_describer():

    print(f"Consonants are {list(consonants.keys())}")
    print(f"Vowels are {list(vowels.keys())}")
    print(f"Voiceless sounds are {list(voiceless.keys())}")
    print(f"Voiced sounds are {list(voiced.keys())}")
    print(f"Dentals are {list(dentals.keys())}")
    print(f"Labials are {list(labials.keys())}")
    print(f"Alveolars are {list(alveolars.keys())}")
    print(f"Palatals are {list(palatals.keys())}")
    print(f"Retroflexes are {list(retroflexes.keys())}")
    print(f"Velars are {list(velars.keys())}")
    print(f"Stops are {list(stops.keys())}")
    print(f"Fricatives are {list(fricatives.keys())}")
    print(f"Affricates are {list(affricates.keys())}")
    print(f"Nasals are {list(nasals.keys())}")
    print(f"Approximants are {list(approximants.keys())}")
    print(f"Laterals are {list(laterals.keys())}")
    print(f"Front vowels are {list(front_vowels.keys())}")
    print(f"Central vowels are {list(central_vowels.keys())}")
    print(f"Back vowels are {list(back_vowels.keys())}")
    print(f"High vowels are {list(high_vowels.keys())}")
    print(f"Mid vowels are {list(mid_vowels.keys())}")
    print(f"Low vowels are {list(low_vowels.keys())}")
    print(f"Rounded sounds are {list(rounded_sounds.keys())}")
    print(f"Unrounded sounds are {list(unrounded_sounds.keys())}")


sounds = sound_importer('sounds.csv')
sound_unpacker()
sound_describer()

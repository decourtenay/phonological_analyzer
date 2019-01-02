high_vowels = ['i', 'y', 'u']
mid_vowels = ['e', 'o']
low_vowels = ['a']
front_vowels = ['i', 'e']
back_vowels = ['o', 'u']
central_vowels = ['a', 'y']

voiceless_consonants = ['p', 'f', 't', 's', 'ts', 'sh', 'ch', 'sj', 'cj', 'k', 'x']
voiced_consonants = ['b', 'v', 'd', 'z', 'dz', 'zh', 'jh', 'zj', 'dj', 'g', 'r', 'l', 'w', 'm', 'n', 'nj', 'j']

dentals = ['t', 'd', 's', 'z', 'ts', 'dz', 'n']
labials = ['p', 'b', 'f', 'v', 'm']
alveolars = ['r', 'l', 'sh', 'zh', 'ch', 'jh', 'r', 'l']
alveopalatals = ['sj', 'zj', 'cj', 'dj', 'nj', 'j']
velars = ['k', 'g', 'x', 'w']

stops = ['p', 'b', 't', 'd', 'k', 'g']
affricates = ['ts', 'dz', 'ch', 'jh', 'cj', 'dj']
fricatives = ['f', 'v', 's', 'z', 'sh', 'zh', 'sj', 'zj', 'x']
approximants = ['w', 'r', 'j']
lateral_approximant = ['l']
nasals = ['m', 'n', 'nj']


class Sound:
    def __init__(self):
        pass

    def print_info(self):
        print(self.description())


class Consonant(Sound):
    def __init__(self, symbol, voicing, place, manner):
        super().__init__()
        self.symbol = symbol
        self.place = place
        self.manner = manner
        self.voicing = voicing

    def description(self):
        self.description = f"/{self.symbol}/ is a {self.voicing} {self.place} {self.manner}."
        return self.description

    def sound_devoicing(self):
        if self.voicing == 'voiced':
            for voiceless_sound in voiceless_consonants:
                pair = [self.symbol, voiceless_sound]
                if set(pair).issubset(set(dentals)) or set(pair).issubset(set(labials)) \
                        or set(pair).issubset(set(alveolars)) or set(pair).issubset(set(alveopalatals)) \
                        or set(pair).issubset(set(velars)):
                    if set(pair).issubset(set(stops)) or set(pair).issubset(set(affricates)) \
                            or set(pair).issubset(set(fricatives)):
                        print(f"The voiceless counterpart of {self.symbol} is {voiceless_sound}")

    def sound_feature_specification(self):
        if self.symbol in voiceless_consonants:
            sound_specification = {'voicing': 'voiceless'}
        elif self.symbol in voiced_consonants:
            sound_specification = {'voicing': 'voiced'}
        if self.symbol in dentals:
            sound_specification.update({'place': 'dental'})
        elif self.symbol in labials:
            sound_specification.update({'place': 'labial'})
        elif self.symbol in alveolars:
            sound_specification.update({'place': 'alveolar'})
        elif self.symbol in alveopalatals:
            sound_specification.update({'place': 'alveopalatal'})
        elif self.symbol in velars:
            sound_specification.update({'place': 'velar'})
        if self.symbol in stops:
            sound_specification.update({'manner': 'stop'})
        elif self.symbol in fricatives:
            sound_specification.update({'manner': 'fricative'})
        elif self.symbol in affricates:
            sound_specification.update({'manner': 'affricate'})
        elif self.symbol in nasals:
            sound_specification.update({'manner': 'nasal'})
        elif self.symbol in approximants:
            sound_specification.update({'manner': 'approximant'})
        print(f"The feature specification for {self.symbol} is {sound_specification}")

class Vowel(Sound):
    def __init__(self, voicing='voiced', frontness='central'):
        super().__init__()
        self.voicing = voicing
        self.frontness = frontness

    def description(self):
        self.description = f"/{self.symbol}/ is a {self.voicing} {self.height} {self.frontness} {self.roundness} vowel."
        return self.description

class HighVowel(Vowel):
    def __init__(self, symbol, frontness, height='high'):
        super().__init__()
        self.symbol = symbol
        self.height = height
        self.frontness = frontness
        if self.frontness == 'back':
            self.roundness = 'rounded'
        else:
            self.roundness = 'unrounded'

    def lower(self):
        old_self_symbol = self.symbol
        if self.frontness == 'front':
            self = MidVowel('e', 'front')
        elif self.frontness == 'back':
            self = MidVowel('o', 'back')
        print(f"The lowered version of /{old_self_symbol}/ is /{self.symbol}/")
        return self

class MidVowel(Vowel):
    def __init__(self, symbol, frontness, height='mid'):
        super().__init__()
        self.height = height
        self.frontness = frontness
        self.symbol = symbol
        if self.frontness == 'back':
            self.roundness = 'rounded'
        else:
            self.roundness = 'unrounded'

    def rise(self):
        old_self_symbol = self.symbol
        if self.frontness == 'front':
            self = HighVowel('i', 'front')
        elif self.frontness == 'back':
            self = HighVowel('u', 'back')
        print(f"The raised version of /{old_self_symbol}/ is /{self.symbol}/")
        return self

class LowVowel(Vowel):
    def __init__(self, symbol, height='low'):
        super().__init__()
        self.height = height
        self.symbol = symbol
        self.roundness = 'unrounded'

# **********************************************************************************************
# The following four functions bypass the need to 'manually' create Sound objects using features
# They make it possible to use symbols (from input or directly entered into the function)
#
# Let the user select the sound to inquire about
# user input > 'x'
# Not to be called directly
def get_answer_from_user():
    answer = input("What is the sound? ")
    return answer


# Create Consonant or Vowel objects from inputted string
# 'x' > Consonant()
# Not to be called directly
def get_sound(answer):
    if answer in front_vowels:
        frontness = 'front'
    elif answer in back_vowels:
        frontness = 'back'
    elif answer in central_vowels:
        frontness = 'central'

    if answer in stops:
        manner = 'stop'
    elif answer in affricates:
        manner = 'affricate'
    elif answer in fricatives:
        manner = 'fricative'
    elif answer in nasals:
        manner = 'nasal'
    elif answer in approximants:
        manner = 'approximant'
    elif answer in lateral_approximant:
        manner = 'lateral approximant'

    if answer in dentals:
        place = 'dental'
    elif answer in labials:
        place = 'labial'
    elif answer in alveolars:
        place = 'alveolar'
    elif answer in alveopalatals:
        place = 'alveopalatal'
    elif answer in velars:
        place = 'velar'

    if answer in voiceless_consonants:
        voicing = 'voiceless'
    elif answer in voiced_consonants:
        voicing = 'voiced'

    if answer in high_vowels:
        sound = HighVowel(answer, frontness)
    elif answer in mid_vowels:
        sound = MidVowel(answer, frontness)
    elif answer in low_vowels:
        sound = LowVowel(answer)
    else:
        sound = Consonant(answer, voicing, place, manner)
    return sound


# Print info for inputted sound (string)
# 'x' > Sound() object > 'Description'
# Call directly
def get_description(sound):
    answer_1 = sound
    sound_1 = get_sound(answer_1)
    sound_1.print_info()


# Print info for sound inputted by user (string)
# input > 'x' > Sound() object > 'Description'
# Call directly
def get_description_for_input():
    answer_1 = get_answer_from_user()
    sound_1 = get_sound(answer_1)
    sound_1.print_info()
# *****************************************************************************************


# Print description for all consonants
# Call directly
def enumerate_consonants():
    consonants = voiceless_consonants + voiced_consonants
    for consonant in consonants:
        get_description(consonant)

# Print voiceless counterparts of voiced obstruents
# Parallel to instance method sound_devoicing() in Consonant class
# Call directly
def devoicing():
    for voiced_sound in voiced_consonants:
        for voiceless_sound in voiceless_consonants:
            pair = [voiced_sound, voiceless_sound]
            if set(pair).issubset(set(dentals)) or set(pair).issubset(set(labials))\
                or set(pair).issubset(set(alveolars)) or set(pair).issubset(set(alveopalatals))\
                    or set(pair).issubset(set(velars)):
                if set(pair).issubset(set(stops)) or set(pair).issubset(set(affricates))\
                        or set(pair).issubset(set(fricatives)):
                    print(f"The voiceless counterpart of {voiced_sound} is {voiceless_sound}")


# Outputs feature specifications for all consonants
# Parallel to instance method sound_feature_specification() in Consonant class
# Call directly
def feature_specification():
    consonants = voiced_consonants + voiceless_consonants
    for sound in consonants:
        if sound in voiceless_consonants:
            sound_specification = {'voicing':'voiceless'}
        elif sound in voiced_consonants:
            sound_specification = {'voicing':'voiced'}
        if sound in dentals:
            sound_specification.update({'place':'dental'})
        elif sound in labials:
            sound_specification.update({'place':'labial'})
        elif sound in alveolars:
            sound_specification.update({'place':'alveolar'})
        elif sound in alveopalatals:
            sound_specification.update({'place':'alveopalatal'})
        elif sound in velars:
            sound_specification.update({'place':'velar'})
        if sound in stops:
            sound_specification.update({'manner':'stop'})
        elif sound in fricatives:
            sound_specification.update({'manner':'fricative'})
        elif sound in affricates:
            sound_specification.update({'manner':'affricate'})
        elif sound in nasals:
            sound_specification.update({'manner':'nasal'})
        elif sound in approximants:
            sound_specification.update({'manner':'approximant'})
        print(f"The feature specification for {sound} is {sound_specification}")


# cons = Consonant('d','voiced','dental','stop')
# cons.print_info()
# cons.sound_devoicing()
# cons.sound_feature_specification()

# get_description('d')
# get_description_for_input()
# enumerate_consonants()
# devoicing()
# feature_specification()

vowel = HighVowel('i','front')
vowel.print_info()
vowel = vowel.lower()
vowel.print_info()
#
# vowel = MidVowel('e','front')
# vowel.print_info()
# vowel = vowel.rise()
# vowel.print_info()
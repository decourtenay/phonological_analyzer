from importer import sound_importer
sounds = sound_importer('sounds.csv')


class Sound:
    def __init__(self):
        pass

    def print_info(self):
        print(self.description())


class Consonant(Sound):
    def __init__(self, sound_type='consonant'):
        super().__init__()
        self.sound_type = sound_type

    def description(self):
        self.description = f"/{self.symbol}/ is a {self.voicing} {self.place} {self.manner}."
        return self.description


class Obstruent(Consonant):
    def __init__(self, voicing='voiceless'):
        super().__init__()
        self.voicing = voicing


class VoicelessObstruent(Obstruent):
    def __init__(self, symbol, place, manner):
        super().__init__()
        self.symbol = symbol
        self.place = place
        self.manner = manner


class VoicedObstruent(Obstruent):
    def __init__(self, symbol, place, manner, voicing='voiced'):
        super().__init__()
        self.symbol = symbol
        self.place = place
        self.manner = manner
        self.voicing = voicing

    def devoice(self):
        old_self_symbol = self.symbol
        for sound in sounds:
            if sound['sound_type'] == 'consonant':
                if sound['place'] == self.place:
                    if sound['manner'] == self.manner:
                        self.symbol = sound['symbol']
                        self = VoicelessObstruent(self.symbol, self.place, self.manner)
                        print(f"The voiceless version of /{old_self_symbol}/ is /{self.symbol}/")
                        return self


class Sonorant(Consonant):
    def __init__(self, symbol, place, manner, voicing='voiced'):
        self.symbol = symbol
        self.voicing = voicing
        self.place = place
        self.manner = manner


class Vowel(Sound):
    def __init__(self, sound_type='vowel', voicing='voiced', frontness='central'):
        super().__init__()
        self.sound_type = sound_type
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

# sound1 = VoicelessObstruent('t', 'dental', 'stop')
# sound1.print_info()
# print('\n')
#
# sound2 = VoicedObstruent('b', 'labial', 'stop')
# sound2.print_info()
# sound2 = sound2.devoice()
# sound2.print_info()
# print('\n')
#
# sound3 = Sonorant('m', 'labial', 'nasal')
# sound3.print_info()
# print('\n')
#
# sound4 = MidVowel('e', 'front')
# sound4.print_info()
# sound4 = sound4.rise()
# sound4.print_info()
# print('\n')

# sound5 = LowVowel('a')
# sound5.print_info()

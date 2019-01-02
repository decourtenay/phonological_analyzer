from importer import sound_importer
sounds = sound_importer('sounds.csv')
from sound_classes import *


def create_instance(symbol):
    for sound in sounds:
        if sound['symbol'] == symbol:
            sound_type = sound['sound_type']
            voicing = sound['voicing']
            place = sound['place']
            manner = sound['manner']
            height = sound['height']
            backness = sound['backness']
            roundness = sound['roundness']
    if sound_type == 'consonant':
        if voicing == 'voiced' and manner == 'approximant' or manner == 'nasal':
            token = Sonorant(symbol, place, manner)
        elif voicing == 'voiceless':
            token = VoicelessObstruent(symbol, place, manner)
        else:
            token = VoicedObstruent(symbol, place, manner)
    else:
        if height == 'high':
            token = HighVowel(symbol, backness)
        elif height == 'mid':
            token = MidVowel(symbol, backness)
        else:
            token = LowVowel(symbol)
    return token


token1 = create_instance('m')
token1.print_info()
token2 = create_instance('d')
token2.print_info()
token3 = create_instance('sj')
token3.print_info()
token4 = create_instance('i')
token4.print_info()
token5 = create_instance('o')
token5.print_info()
token6 = create_instance('a')
token6.print_info()
print('\n')
token2 = token2.devoice()
token2.print_info()
print('\n')
token4 = token4.lower()
token4.print_info()
print('\n')
token5 = token5.rise()
token5.print_info()


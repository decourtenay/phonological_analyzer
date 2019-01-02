#  Not executable directly

def sound_importer(csvfile):

    import csv
    global sounds
    sounds = []
    with open(csvfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sound = dict(row)
            sounds.append(sound)
    return sounds

# print(sound_importer('sounds.csv'))
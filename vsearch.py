def search4vowels(word):
    vowels=set('aeiou')
    return vowels.intersection(set(word))
def search4letters(word,letters='aeiou'):
    return set(letters).intersection(set(word))

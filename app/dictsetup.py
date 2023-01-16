from pdf import *

def convert(isolatedKanji):
    frequency = {}

    for kanji in isolatedKanji:
        if kanji in frequency:
            frequency[kanji] += 1
        else:
            frequency[kanji] = 1

    sortedKanji = sorted(frequency.items(), key = lambda x : x[1], reverse = True)
    convertedSortedKanji = dict(sortedKanji)
    return convertedSortedKanji
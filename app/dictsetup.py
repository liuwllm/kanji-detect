from pdf import *

frequency = {}

for kanji in pdfIsolatedKanji:
    if kanji in frequency:
        frequency[kanji] += 1
    else:
        frequency[kanji] = 1

sortedKanji = sorted(frequency.items(), key = lambda x : x[1], reverse = True)
convertedSortedKanji = dict(sortedKanji)
print(convertedSortedKanji)
from dictsetup import *
from jisho_api.kanji import Kanji

class kanjiInfo:
    def __init__(self, kanji, strokes, meanings, kunReadings, onReadings, radicals):
        self._kanji = kanji
        self._strokes = strokes
        self._meanings = meanings
        self._kunReadings = kunReadings
        self._onReadings = onReadings
        self._radicals = radicals
    def getKanji(self):
        return self._kanji
    def getStrokes(self):
        return self._strokes
    def getMeanings(self):
        return self._meanings
    def getKunReadings(self):
        return self._kunReadings
    def getOnReadings(self):
        return self._onReadings
    def getRadicals(self):
        return self._radicals
    def setKanji(self, newKanji):
        self._kanji = newKanji
    def setStrokes(self, newStrokes):
        self._strokes = newStrokes
    def setMeanings(self, newMeanings):
        self._meanings = newMeanings
    def setKunReadings(self, newKunReadings):
        self._kunReadings = newKunReadings
    def setOnReadings(self, newOnReadings):
        self._onReadings = newOnReadings
    def setRadicals(self, newRadicals):
        self._radicals = newRadicals

def jishoLookup(isolatedKanji):
    kanjiArray = []

    convertedKanji = convert(isolatedKanji)

    for sortedKanji in convertedKanji:
        kanjiArray.append([
            Kanji.request(sortedKanji).data.kanji, 
            Kanji.request(sortedKanji).data.strokes, 
            Kanji.request(sortedKanji).data.main_meanings, 
            Kanji.request(sortedKanji).data.main_readings.kun, 
            Kanji.request(sortedKanji).data.main_readings.on, 
            Kanji.request(sortedKanji).data.radical.parts
        ])
    
    return kanjiArray

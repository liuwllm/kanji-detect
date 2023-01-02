kanjiRanges = [
    {"from": ord(u"\u4e00"), "to": ord(u"\u9faf")},
    {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")}
]

def isKanji(char):
    return any([range["from"] <= ord(char) <= range["to"] for range in kanjiRanges])

def findKanji(string):
    newString = ""
    for char in string:
        if isKanji(char):
            newString += char
    return newString
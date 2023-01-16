from jisho import *
import csv

outputFile = "test.csv"

def csvWrite(fileLocation, outputFile):
    allData = jishoLookup(pdfExtract(fileLocation))

    csvFile = open(outputFile, "w+", newline = '')

    with csvFile:
        write = csv.writer(csvFile)
        write.writerow(["Kanji Character", "Strokes", "Meaning", "Kunyomi Readings", "Onyomi Readings", "Radicals"])
        write.writerows(allData)

csvWrite(testLocation, outputFile)
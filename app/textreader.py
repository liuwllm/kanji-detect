import tika
tika.initVM()
from tika import parser

from app.kanjidetection import *

def pdfExtract(fileLocation):
    # Using tika to extract text from pdf file
    parsed = parser.from_file(fileLocation)
    
    # Splitting text into individual sentences & storing in content array
    content = parsed['content'].split("\n!?.！？。")

    return content

def txtExtract(fileLocation):
    # Opening txt file
    parsed = open(fileLocation, "r")

    # Splitting text into individual sentences & storing in content array
    content = []
    tmpContent = parsed.readlines()
    for line in tmpContent:
        splitLines = line.split("\n!?.！？。")
        for line in splitLines:
            content.append(line)

    return content

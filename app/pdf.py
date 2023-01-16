import tika
tika.initVM()
from tika import parser

from kanji import *

testLocation = "./app/test.pdf"

def pdfExtract(fileLocation):
    parsed = parser.from_file(fileLocation)

    parsed['content'] = parsed['content'].strip().replace('\n', '')
    
    return(findKanji(parsed['content']))
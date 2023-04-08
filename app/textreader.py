import tika
tika.initVM()
from tika import parser

from kanji import *

def pdfExtract(fileLocation):
    parsed = parser.from_file(fileLocation)

    parsed['content'] = parsed['content'].strip().replace('\n', '')
    
    return(findKanji(parsed['content']))
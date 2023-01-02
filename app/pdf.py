import tika
tika.initVM()
from tika import parser

from kanji import *

parsed = parser.from_file('./app/test.pdf')

parsed['content'] = parsed['content'].strip().replace('\n', '')

pdfIsolatedKanji = findKanji(parsed['content'])


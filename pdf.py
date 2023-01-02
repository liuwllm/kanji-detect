import tika
tika.initVM()
from tika import parser

from kanji import *

parsed = parser.from_file('test.pdf')

parsed['content'] = parsed['content'].strip().replace('\n', '')

print(findKanji(parsed['content']))


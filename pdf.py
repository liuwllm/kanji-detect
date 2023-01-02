import tika
tika.initVM()
from tika import parser

parsed = parser.from_file('test.pdf')

parsed['content'] = parsed['content'].strip().replace('\n', '')

print(parsed)
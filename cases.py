import re
from caseconverter import *


def no_punctuation(s):
    return re.sub(r'[^\w\s]', ' ', s)


def simple_by_delimiter(s, delimiter):
    return snakecase(no_punctuation(s)).replace('_', delimiter)


cases = {
    'space': lambda s: simple_by_delimiter(s, ' '),
    'upper': lambda s: s.upper(),
    'lower': lambda s: s.lower(),
    'snake':  snakecase,
    'camel':  camelcase,
    'pascal': pascalcase,
    'kebab':  kebabcase,
    'cobol':  cobolcase,
    'macro':  macrocase,
    'dot': lambda s: simple_by_delimiter(s, '.'),
    'path': lambda s: simple_by_delimiter(s, '/'),
    'flat':   flatcase,
}

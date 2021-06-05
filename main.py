import re
import sys


class SentenceValidation:
    regular_expressions = {
        'even-binary': '^([01]{2})*$',
        'twice-101': '(.*101){2}',
        'starts-ends-with': '^01[01]*10$'
    }

    def __init__(self):
        self._type = None

    def set_type(self, type):
        self._type = type

    def is_valid(self, sentence):
        regex = SentenceValidation.regular_expressions.get(self._type)
        return bool(re.match(regex, sentence))


if __name__ == '__main__':
    type, sentence = sys.argv[1:3]

    if type in SentenceValidation.regular_expressions.keys():
        sentence_validation = SentenceValidation()
        sentence_validation.set_type(type)
        if sentence_validation.is_valid(sentence):
            print(f'{sentence} is valid.')
            sys.exit(0)
        print(f'{sentence} is invalid')
    else:
        print('This type is invalid.')
        sys.exit(1)

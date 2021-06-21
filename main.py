import re
import sys


class SentenceValidation:
    regular_expressions = {
        'even-binary': '^([01]{2}){2,}$',
        'twice-101': '([01]*(101)[01]*){2,}',
        'starts-with-01-and-ends-with-10': '^01[01]*10$',
        'any-binary-sequence': '^[01]{1,}$',
        '0110-and-1001': '^(0110|1001)$'
    }

    def __init__(self):
        self._type = None

    def set_type(self, type):
        self._type = type

    def is_valid(self, sentence):
        regex = SentenceValidation.regular_expressions.get(self._type)
        return bool(re.match(regex, sentence))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        regex_type, sentence = sys.argv[1:3]

        if regex_type in SentenceValidation.regular_expressions.keys():
            sentence_validation = SentenceValidation()
            sentence_validation.set_type(regex_type)
            if sentence_validation.is_valid(sentence):
                print(f'{sentence} is valid.')
                sys.exit(0)
            print(f'{sentence} is invalid')
            sys.exit(1)

        print('This type is invalid.')
        with open('./help') as file:
            print(file.read())
        sys.exit(1)

    else:
        with open('./help') as file:
            print(file.read())
        sys.exit(1)

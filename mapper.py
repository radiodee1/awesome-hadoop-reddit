#!/usr/bin/env python


import sys
import re
import json
#from string import punctuation

EMPTY = '--'


def read_input(file):
    list = []
    for line in file:

        try:
            row = json.loads(line)
        except:
            row['body'] = ''
            pass

        line = row['body']

        #line = re.sub(r'(?<=['+punctuation+'])\s+(?=[A-Z])', '\n', line)
        #return line.split('\n')
        yield re.split(r'[.]|[\r]|[?]|[!]', line)


def main(separator='\t'):
    last_sentence = EMPTY

    data = read_input(sys.stdin)

    for lines in data:

        for sentence in lines:
            if last_sentence == EMPTY or len(sentence.strip()) == 0 or len(last_sentence.strip()) == 0:
                last_sentence = sentence
                continue

            sentence = sentence.strip()
            print ('%s%s%s%s%d' % (last_sentence, separator, sentence, separator, 1))
            last_sentence = sentence

if __name__ == "__main__":
    main()

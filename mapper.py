#!/usr/bin/env python


import sys
import re
import json


def read_input(file):
    for line in file:
        # split the line into words
        row = json.loads(line)

        body = row['body']

        line = body

        yield re.split(r'[.]|[\r]', line)

def main(separator='\t'):
    last_sentence = ''

    data = read_input(sys.stdin)

    for lines in data:

        for sentence in lines:
            sentence = sentence.strip()
            print ('%s%s%s%s%d' % (last_sentence, separator, sentence, separator, 1))
            last_sentence = sentence

if __name__ == "__main__":
    main()

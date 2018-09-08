#!/usr/bin/env python


import sys
import re
import json
from string import punctuation

EMPTY = '--'


def read_input(file):
    list = []
    for line in file:

        try:
            row = json.loads(line)
        except:
            row = {}
            row['body'] = ''
            pass

        line = row['body'].encode('ascii', 'replace') ## ignore?
        line = re.sub(r'[\t]|[\r]|[\n]','', line)

        line = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', line)
        list.extend(line)

    return list


def main(separator='\t'):
    last_sentence = EMPTY

    data = read_input(sys.stdin)

    for sentence in data:
        if True:

            sentence = sentence.strip().replace('\r', '')

            if last_sentence == EMPTY or len(sentence.strip()) == 0 or len(last_sentence.strip()) == 0:
                last_sentence = sentence
                continue

            print ('%s%s%s%s%d' % (last_sentence, separator, sentence, separator, 1))
            last_sentence = sentence

if __name__ == "__main__":
    main()

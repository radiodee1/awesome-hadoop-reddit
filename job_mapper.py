#!/usr/bin/python3.6

from __future__ import absolute_import
#from __future__ import print_function
import sys
import re
import json
#from string import punctuation


EMPTY = '--'


def read_input(file):
    list = []
    key = ''
    for line in file:

        try:
            row = json.loads(line)
        except :
            #print('skip')
            row = {} # dict()
            row['body'] = ''
            row['author'] = ''
            pass

        key = row['author']
        #line = row['body'].encode('ascii', 'replace') ## ignore?
        line = row['body']
        line = re.sub(r'[\t]|[\r]|[\n]','', line)
        line = re.sub(r'\s+', ' ', line)

        line = re.sub('\?', ' ? ', line)
        line = re.sub('\.', ' . ', line)
        line = re.sub('!', ' ! ', line)

        line = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', line)
        #line = line.split('.')
        list.extend(line)

    return [key, list]


def main(_, data):

    separator = '\t'
    last_sentence = EMPTY

    data = read_input([data])
    key = data[0]
    data = data[1]
    data.append(str(1))
    yield key, separator.join(data)
    #print(key, separator.join(data))
    '''
    for sentence in data:
        if True:

            sentence = sentence.strip().replace('\r', '')

            if last_sentence == EMPTY or len(sentence.strip()) == 0 or len(last_sentence.strip()) == 0:
                last_sentence = sentence
                continue

            yield (key,  last_sentence.strip() + separator + sentence.strip() + separator + str(1) )
            last_sentence = sentence
    '''

if __name__ == "__main__":
    main()

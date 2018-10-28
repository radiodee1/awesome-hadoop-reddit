#!/usr/bin/python3.6

from __future__ import absolute_import
from itertools import groupby
from operator import itemgetter
import sys
import re

EMPTY = '--'


def count_faults(content):
    c = content.lower().strip()

    c = re.sub("[\"`]", "'", c)

    punctuation =  len(re.findall(r'^([!]|[\?]|[\.])',c))

    c = c.split(' ')

    length_sent = 1
    length_start = len(c)
    if length_start >= 4: length_sent = 0

    begin = 0
    end = 0
    w_period = 0
    b_e_w_period = 0
    both = 0
    amp = 0
    link = 0
    link2 = 0
    www = 0
    odd = 0
    double = 0
    control = 0
    word = 0

    for z in c:
        begin += len(re.findall(r"^[']+([^']*)", z))
        end += len(re.findall(r"(\w+)[']+$", z))
        w_period += len(re.findall(r"^(\w+)'\.$", z))
        b_e_w_period += len(re.findall(r"^'(\w+)'\.$", z))
        both += len(re.findall(r"^[']+([^']*)[']+$", z))
        amp += len(re.findall(r"&(\w+);", z))  ## anywhere in word
        link += len(re.findall(r"^http(\w+)", z))
        link2 += len(re.findall(r"^\(http(\w+)", z))
        www += len(re.findall(r"^www", z))
        odd += len(re.findall(r"([$%0123456789+=^;:~_/\\])(\w*)", z))
        double += len(re.findall(r"(['])(['])+", z))
        control += len(re.findall(r'[\x00-\x1f]',z))

        if z == 'm' or z == 's' or z == 't': word = 1

    out = begin + end + w_period + b_e_w_period + both + amp + link + link2 + www + odd + double + length_sent + control
    out += punctuation
    out += word
    #print(c, 'c', out)

    return out

def clean(text):
    text = re.sub('[][)(\n\r#@*^><:|{},]', '', text)
    #text = re.sub('\?', ' ? ', text)
    #text = re.sub('\.', ' . ', text)
    #text = re.sub( '!', ' ! ', text)
    return text


def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator)

def main(key, data):
    separator = '\t'

    data = read_mapper_output(data, separator=separator)
    last_sentence = EMPTY

    #print(list(data))

    try:

        for z in data:
            #print(len(z), 'len', key)
            for sentence in z:
                if True:
                    #print(sentence)
                    sentence = sentence.strip().replace('\r', '')

                    if last_sentence == EMPTY or len(sentence.strip()) == 0 or len(last_sentence.strip()) == 0:
                        last_sentence = sentence
                        continue

                    sentence = clean(sentence).strip()
                    last_sentence = clean(last_sentence).strip()

                    total_count = count_faults(sentence) + count_faults(last_sentence)

                    if total_count == 0:
                        yield (key, last_sentence.strip() + separator + sentence.strip() + separator + str(1))
                    last_sentence = sentence

    except IndexError:
        print('Index Error')
        pass

if __name__ == "__main__":
    main()

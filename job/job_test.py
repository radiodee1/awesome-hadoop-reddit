#!/usr/bin/python3.6

from __future__ import absolute_import

import json
import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep
import re


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

class JobTest(MRJob):

    INPUT_PROTOCOL  = mrjob.protocol.TextValueProtocol
    OUTPUT_PROTOCOL = mrjob.protocol.TextValueProtocol
    INTERNAL_PROTOCOL = mrjob.protocol.TextProtocol

    def steps(self):
        return [
            MRStep(mapper=self.map,
                   #combiner=self.combiner_count_words,
                   reducer=self.reduce
                   ),
        ]

    def map(self, _, data):
        separator = '\t'
        last_sentence = EMPTY

        data = read_input([data])
        key = data[0]
        data = data[1]
        data.append(str(1))
        yield key, separator.join(data)
        # print(key, separator.join(data))

    def reduce(self, key, data):
        separator = '\t'

        data = read_mapper_output(data, separator=separator)
        last_sentence = EMPTY

        # print(list(data))

        try:

            for z in data:
                # print(len(z), 'len', key)
                for sentence in z:
                    if True:
                        # print(sentence)
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

if __name__ == '__main__':
    JobTest.run()
#!/usr/bin/env python3.6


from itertools import groupby
from operator import itemgetter
import sys
import re

def clean(content):
    c = content.lower().strip()
    #c = re.sub('[][)(\n\r#@*^><:|{}]', ' ', c)
    c = re.sub("[\"`]", "'", c)
    c = c.split(' ')

    length_sent = len(c)
    if length_sent >= 2: length_sent = 0

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

    out = begin + end + w_period + b_e_w_period + both + amp + link + link2 + www + odd + double + length_sent

    return out

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator,4)

def main(separator='\t'):

    data = read_mapper_output(sys.stdin, separator=separator)

    try:
        for current_words, group in groupby(data, itemgetter(0,1,2)):
            current_words = list(current_words)
            current_words[0] = re.sub('[][)(\n\r#@*^><:|{}]', ' ', current_words[0])
            current_words[1] = re.sub('[][)(\n\r#@*^><:|{}]', ' ', current_words[1])

            try:
                total_count = clean(current_words[0]) + clean(current_words[1])
                #total_count = sum(int(count) for current_words, count in group)
                #total_count = sum(int(current_words[2]) for current_words in group)
                if total_count == 0:
                    print ("%s%s%s%s%d" % (current_words[0].lower(), separator, current_words[1].lower(), separator, total_count))
            except ValueError:
                # count was not a number, so silently discard this item
                pass
    except IndexError:
        pass

if __name__ == "__main__":
    main()

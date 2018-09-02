#!/usr/bin/env python3.6


from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator,4)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items

    try:
        for current_words, group in groupby(data, itemgetter(0,1,2)):

            try:
                #total_count = sum(int(count) for current_words, count in group)
                total_count = sum(int(current_words[2]) for current_words in group)
                print ("%s%s%s%s%d" % (current_words[0], separator, current_words[1], separator, total_count))
            except ValueError:
                # count was not a number, so silently discard this item
                pass
    except IndexError:
        pass

if __name__ == "__main__":
    main()

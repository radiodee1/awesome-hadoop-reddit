#!/usr/bin/env python

import argparse
import os
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split raw reddit file.')
    parser.add_argument('--filename',help='name of file to split.')
    parser.add_argument('--start',help='optional starting line number.')
    parser.add_argument('--length', help='length of output file. (default: 500)')
    parser.add_argument('--triplets',help='record triplets', action='store_true')
    parser.add_argument('--pairs', help='record pairs', action='store_true')
    parser.add_argument('--dummy-question', help='record single dummy question')

    args = parser.parse_args()
    args = vars(args)

    print(args)

    arg_filename = 'RC_2017-11'
    arg_start = 0
    arg_length = -1

    arg_triplets = False
    arg_pairs = False
    arg_question = ''
    arg_processed = False

    if args['filename'] is not None:
        arg_filename = str(args['filename'])

    if not os.path.isfile(arg_filename):
        arg_filename = '../hadoop-input/' + arg_filename
    if not os.path.isfile(arg_filename):
        print('bad path')
        exit()

    if args['start'] is not None:
        arg_start = int(args['start'])
        print('start:', arg_start)

    if args['length'] is not None:
        arg_length = int(args['length'])
        print('length:', arg_length)

    if args['triplets'] == True:
        arg_triplets = True
        arg_processed = True

    if args['pairs'] == True:
        arg_pairs = True
        arg_processed = True
        arg_triplets = False

    if args['dummy_question'] is not None:
        arg_question = str(args['dummy_question'])
        arg_processed = True

    arg_destination = arg_filename + '.output.txt'

    if not arg_processed:
        if arg_length <= 0:
            arg_length = 500

        lines = []
        with open(arg_filename,'r') as z:
            num = 0
            for line in z:
                if num >= arg_start and num < arg_start + arg_length:
                    lines.append(line)
                if num > arg_start + arg_length:
                    break
                num += 1
            z.close()

        with open(arg_destination,'w') as z:
            for line in lines:
                z.write(line)
                if not line.endswith('\n'):
                    z.write('\n')
            z.close()
    else:
        ''' do split file '''
        if arg_length <= 0:
            arg_length = 0
        pass


    print('done.')
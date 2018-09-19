#!/usr/bin/env python

import argparse
import os
import sys

hparams = {
    'save_dir': "~/",
    'data_dir': "~/",
    'test_name': "test",
    'train_name': "train",
    'valid_name':'valid',
    'src_ending': "from",
    'tgt_ending': "to",
    'question_ending':'ques',
    'babi_name':'babi'
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split raw reddit file.')
    parser.add_argument('--filename',help='name of file to split.')
    parser.add_argument('--start',help='optional starting line number.')
    parser.add_argument('--length', help='length of output file. (default: 500)')
    parser.add_argument('--triplets',help='record triplets', action='store_true')
    parser.add_argument('--pairs', help='record pairs', action='store_true')
    parser.add_argument('--dummy-question', help='record single dummy question')
    parser.add_argument('--mode', help='"test", "train", or "valid" (default = "train")')

    args = parser.parse_args()
    args = vars(args)

    print(args)

    arg_filename = 'RC_2017-11'
    arg_start = 0
    arg_length = -1

    arg_triplets = False
    arg_pairs = False
    arg_question = None #''
    arg_processed = False

    arg_mode = hparams['train_name']

    arg_destination_context = ''
    arg_destination_question = ''
    arg_destination_target = ''

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
        arg_pairs = False
        arg_processed = True

    if args['pairs'] == True:
        arg_pairs = True
        arg_processed = True
        arg_triplets = False

    if args['dummy_question'] is not None:
        arg_question = str(args['dummy_question'])
        arg_processed = True

    if args['mode'] is not None:
        arg_mode = str(args['mode'])
        arg_processed = True
        if arg_mode != 'train' and arg_mode != 'test' and arg_mode != 'valid':
            print('bad mode')
            exit()

    arg_destination = arg_filename + '.output.txt'

    if not arg_processed:
        if arg_length <= 0:
            arg_length = 500

        ''' do split raw file '''
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
        ''' do split processed file '''
        if arg_length <= 0:
            arg_length = 0

        url = arg_destination.split('/')
        url = '/'.join(url[0:-1])
        print(url)
        arg_destination_context = url + '/' + arg_mode +'.'+ hparams['src_ending']
        arg_destination_target = url + '/' + arg_mode + '.' + hparams['tgt_ending']
        arg_destination_question = url + '/' +arg_mode + '.' + hparams['question_ending']
        pass

        with open(arg_filename, 'r') as z:
            num = 0
            src = open(arg_destination_context, 'w')
            tgt = open(arg_destination_target, 'w')

            if arg_triplets:
                ques = open(arg_destination_question, 'w')

            for line in z:
                if num >= arg_start and (arg_length == 0 or num < arg_start + arg_length):
                    line = line.split('\t')
                    src.write(line[0])
                    if not line[0].endswith('\n'):
                        src.write('\n')
                    if arg_triplets:
                        if arg_question is not None and arg_question != '':
                            line[0] = arg_question
                        ques.write(line[0])
                        if not line[0].endswith('\n'):
                            ques.write('\n')
                    tgt.write(line[1])
                    if not line[1].endswith('\n'):
                        tgt.write('\n')

                if arg_length != 0 and num > arg_start + arg_length:
                    print('early stop')
                    break

                num += 1
            src.close()
            tgt.close()
            if arg_triplets:
                ques.close()
        z.close()


    print('done.')
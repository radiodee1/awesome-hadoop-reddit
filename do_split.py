#!/usr/bin/env python3.6

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
    'babi_name':'babi',
    'eol': 'eol'
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='split raw reddit file.')
    parser.add_argument('--filename',help='name of file to split.')
    parser.add_argument('--start',help='optional starting line number.')
    parser.add_argument('--length', help='length of output file. (default: 500)')
    parser.add_argument('--triplets',help='record triplets', action='store_true')
    parser.add_argument('--pairs', help='record pairs', action='store_true')
    parser.add_argument('--dummy-question', help='record single dummy question')
    parser.add_argument('--mode', help='"test", "train", or "valid" - "test.big" and "test.babi" allowed (default = "train")')
    parser.add_argument('--zip-file', help='name of zip file to archive to')
    parser.add_argument('--autoencode', help='setup files for autoencode operation.', action='store_true')
    parser.add_argument('--stagger', help='stagger input for P.O.S.-style training.', action='store_true')

    args = parser.parse_args()
    args = vars(args)

    print(args)

    arg_filename = 'RC_2017-11'
    arg_start = 0
    arg_length = -1

    arg_triplets = False
    arg_pairs = False
    arg_question = None
    arg_processed = False
    arg_zip = None #'train-files'
    arg_filelist = []
    arg_autoencode = False
    arg_stagger = False

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
            if arg_mode != 'train.babi' and arg_mode != 'test.babi' and arg_mode != 'valid.babi':
                if arg_mode != 'train.big' and arg_mode != 'test.big' and arg_mode != 'valid.big':
                    print('bad mode')
                    exit()

    if args['zip_file'] is not None:
        arg_zip = str(args['zip_file'])

    if args['autoencode'] == True:
        arg_autoencode = True

    if args['stagger'] == True:
        arg_stagger = True

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
        arg_destination_context = url + '/' + arg_mode + '.' + hparams['src_ending']
        arg_destination_target = url + '/' + arg_mode + '.' + hparams['tgt_ending']
        arg_destination_question = url + '/' + arg_mode + '.' + hparams['question_ending']

        args_end_string = hparams['eol'] + ' ' + hparams['eol']
        pass

        with open(arg_filename, 'r') as z:
            num = 0
            src = open(arg_destination_context, 'w')
            tgt = open(arg_destination_target, 'w')
            arg_filelist.append(arg_destination_context.split('/')[-1])
            arg_filelist.append(arg_destination_target.split('/')[-1])

            if arg_triplets:
                ques = open(arg_destination_question, 'w')
                arg_filelist.append(arg_destination_question.split('/')[-1])

            if arg_stagger:
                print('stagger output.')

            for line in z:
                save = ''
                if num >= arg_start and (arg_length == 0 or num < arg_start + arg_length):
                    line = line.split('\t')

                    if not arg_stagger:

                        src.write(line[0])
                        save = line[0][:]
                        if not line[0].endswith('\n'):
                            src.write('\n')
                        if arg_triplets:
                            if arg_question is not None and arg_question != '':
                                line[0] = arg_question
                            ques.write(line[0])
                            if not line[0].endswith('\n'):
                                ques.write('\n')
                        if arg_autoencode: line[1] = save #line[0]
                        tgt.write(line[1])
                        if not line[1].endswith('\n'):
                            tgt.write('\n')

                    else:
                        src_stagger = ''
                        tgt_stagger = ''
                        ques_stagger = ''
                        save = line[0][:]
                        save_lst = save.split(' ')
                        tgt_lst = line[1].split(' ')
                        for i in range(len(save_lst)):

                            word = save_lst[i]

                            if i < len(tgt_lst): ii = i
                            else: ii = len(tgt_lst) - 1

                            ques_stagger = word
                            if len(src_stagger) > 0: src_stagger += ' '

                            src_stagger += word

                            src.write(src_stagger)
                            save = src_stagger
                            if not src_stagger.endswith('\n'):
                                src.write('\n')
                            if arg_triplets:
                                if arg_question is not None and arg_question != '':
                                    ques_stagger = arg_question
                                ques.write(ques_stagger)
                                if not ques_stagger.endswith('\n'):
                                    ques.write('\n')
                            tgt_stagger = tgt_lst[ii]
                            if arg_autoencode: tgt_stagger = word #save  # line[0]
                            tgt.write(tgt_stagger)
                            if not tgt_stagger.endswith('\n'):
                                tgt.write('\n')

                            if i != 0: num += 1

                            if arg_length != 0 and num > arg_start + arg_length:
                                print('early stop')
                                break

                        src.write(args_end_string + '\n')
                        tgt.write(hparams['eol'] + '\n')
                        if arg_triplets:
                            ques.write(args_end_string + '\n')
                        pass

                if arg_length != 0 and num > arg_start + arg_length:
                    print('early stop')
                    break

                num += 1
            src.close()
            tgt.close()
            if arg_triplets:
                ques.close()
        z.close()

        if arg_zip is not None:
            os.chdir(url)
            if len(arg_filelist) > 0:
                os.system('zip ' + arg_zip.strip() + '.zip ' + ' '.join(arg_filelist))
            pass

    print('done.')
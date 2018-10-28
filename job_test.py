#!/usr/bin/python3.6

import job_mapper
import job_reducer

import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")


class JobTest(MRJob):

    INPUT_PROTOCOL  = mrjob.protocol.TextValueProtocol
    OUTPUT_PROTOCOL = mrjob.protocol.TextValueProtocol
    INTERNAL_PROTOCOL = mrjob.protocol.TextProtocol

    def steps(self):
        return [
            MRStep(mapper=job_mapper.main,
                   #combiner=self.combiner_count_words,
                   reducer=job_reducer.main
                   ),
            #MRStep(reducer=self.reducer_find_max_word)
        ]




if __name__ == '__main__':
    JobTest.run()
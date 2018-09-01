#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

STREAM=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar

$HADOOP_HOME/bin/hadoop jar $STREAM -input input_dir -output output_dir -mapper < ./mapper.py -reducer < ./reducer.py


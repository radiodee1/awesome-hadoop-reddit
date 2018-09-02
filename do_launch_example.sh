#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

STREAM=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar

$HADOOP_HOME/bin/hadoop jar $STREAM -input /opt/hadoop/input_dir/* -output /opt/hadoop/output_dir -mapper  ./mapper.py -reducer  ./reducer.py #-files ./reducer.py,./mapper.py 



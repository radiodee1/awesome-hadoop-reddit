#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

#STREAM=$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar

$HADOOP_HOME/bin/hadoop dfs -rm -r ~/hadoop-output

#$HADOOP_HOME/bin/hadoop jar $STREAM -input /home/hadoop/hadoop-input -output /home/hadoop/hadoop-output -mapper  ./mapper.py -reducer  ./reducer.py

python3.6 job_test.py -r hadoop < ../raw/RC_2017-11 > out.txt



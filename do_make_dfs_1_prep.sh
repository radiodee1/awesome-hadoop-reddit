#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

mkdir -p /home/hadoop/hdfs ~/hadoop-input ~/hadoop-output 

$HADOOP_HOME/bin/hadoop namenode -format


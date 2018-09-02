#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

sudo mkdir -p /opt/hadoop/tmp ../hadoop-input ../hadoop-output

sudo chown hadoop:hadoop /opt/hadoop/tmp ../hadoop-input ../hadoop-output

$HADOOP_HOME/bin/hadoop namenode -format


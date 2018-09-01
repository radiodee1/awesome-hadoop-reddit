#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

sudo mkdir -p /opt/hadoop/tmp /opt/hadoop/input_dir /opt/hadoop/output_dir

sudo chown hadoop:hadoop /opt/hadoop/tmp /opt/hadoop/input_dir /opt/hadoop/output_dir

$HADOOP_HOME/bin/hadoop namenode -format


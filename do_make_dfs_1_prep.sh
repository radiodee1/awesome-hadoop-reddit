#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

sudo mkdir -p /opt/hadoop/tmp ~/hadoop-input 

sudo chown hadoop:hadoop /opt/hadoop/tmp ~/hadoop-input 

$HADOOP_HOME/bin/hadoop namenode -format


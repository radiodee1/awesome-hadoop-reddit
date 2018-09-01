#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

sudo mkdir -p /opt/hadoop/tmp
sudo chown hadoop:hadoop /opt/hadoop/tmp
$HADOOP_HOME/bin/hadoop namenode -format


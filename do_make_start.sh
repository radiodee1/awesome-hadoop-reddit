#!/bin/bash

export HADOOP_HOME=/usr/local/hadoop

#$HADOOP_HOME/sbin/start-dfs.sh
echo
$HADOOP_HOME/sbin/start-all.sh
echo
$HADOOP_HOME/sbin/start-yarn.sh


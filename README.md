# hadoop-reddit
scrape reddit with hadoop

### Note:
There are two sets of code in this package. One set uses the java streaming api alone.
One set uses streaming but also uses a python library called 'MRJob'. This second set
is surely more interesting and uses code from the first set. Below is
documentation for running both code examples.

## Instuctions - Streaming API:
1. execute download script - `do_make_reddit_download.sh`
2. execute download unzip script - `do_make_reddit_unzip.sh`
3. execute data prep script as root - `do_make_dfs_1_prep.sh`
4. start hadoop - `do_make_start.sh`
5. execute data copy script - `do_make_dfs_2_copy.sh`
6. move to streaming directory - `cd stream`
7. execute hadoop run script - `do_launch_mr.sh`
8. return to project base directory - `cd ..`
9. examine data - `do_make_dfs_3_examine.sh`
10. stop hadoop - `do_make_stop.sh`

## Instuctions - MRJob:
1. execute download script - `do_make_reddit_download.sh`
2. execute download unzip script - `do_make_reddit_unzip.sh`
3. execute data prep script as root - `do_make_dfs_1_prep.sh`
4. start hadoop - `do_make_start.sh`
5. execute data copy script - `do_make_dfs_2_copy.sh`
5. move to job directory - `cd job`
6. execute hadoop run script - `do_launch_mrjob.sh`
7. return to project base directory - `cd ..`
7. examine data - `head job/out.txt`
8. stop hadoop - `do_make_stop.sh`

## File System:
* hadoop user - `/home/hadoop/`
* hadoop project - `/home/hadoop/hadoop-reddit/`
* project input - `/home/hadoop/hadoop-input/`
* project hdfs output - `/home/hadoop/hadoop-output/` (note: not in ext4)
* hadoop install directory - `/usr/local/hadoop/`
* hadoop hdfs directory - `/opt/hadoop/tmp/` (property: hadoop.tmp.dir)

Ubuntu 18.04, hadoop 3.1.1

## Environment Vars:
* `export HADOOP_HOME=/usr/local/hadoop`
* `export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/`

## Script - `do_make_dfs_0_scrap.sh`:
Use this option if you exited the hadoop programs in a less than graceful way. If the dfs is not shut down properly from the last session this script clears the directory with the dfs file system. You will loose any data that you copied to the dfs but you will be able to copy in new data and start over.

## Other Commands:
* `$HADOOP_HOME/bin/hadoop dfs -get /home/hadoop/hadoop-output/part* ~/.` - This copies your output to the root of the home directory for the hadoop user.
* `$HADOOP_HOME/bin/hadoop dfs -cat /home/hadoop/hadoop-output/*` - This displays all the output on the screen.

I modified `yarn-site.xml` with the following contents:
```
  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>

  <property>
    <name>yarn.nodemanager.aux-services.mapreduce_shuffle.class</name>
    <value>org.apache.hadoop.mapred.ShuffleHandler</value>
  </property>
```


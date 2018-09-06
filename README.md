# hadoop-reddit
scrape reddit for hadoop

## Instuctions:
* execute download script - `do_make_reddit_download.sh`
* execute download unzip script - `do_make_reddit_unzip.sh`
* execute data prep script as root - `do_make_dfs_1_prep.sh`
* start hadoop - `do_make_start.sh`
* execute data copy script - `do_make_dfs_2_copy.sh`
* execute hadoop run script - `do_launch_mr.sh`
* examine data - `do_make_dfs_3_examine.sh`
* stop hadoop - `do_make_stop.sh`

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

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
* hadoop install directory - `/usr/local/hadoop`
* hadoop hdfs directory - `/opt/hadoop/tmp/`

Ubuntu 18.04, hadoop 3.1.1

$HADOOP_HOME/bin/hadoop dfs -mkdir -p ~/hadoop-input 
$HADOOP_HOME/bin/hadoop dfs -copyFromLocal ./data/*  ~/hadoop-input
#$HADOOP_HOME/bin/hadoop dfs -put ./data/*.txt ~/hadoop-input



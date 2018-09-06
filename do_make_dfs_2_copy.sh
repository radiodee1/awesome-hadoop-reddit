echo "This may take some time!"

$HADOOP_HOME/bin/hadoop dfs -mkdir -p ~/hadoop-input 
$HADOOP_HOME/bin/hadoop dfs -copyFromLocal ~/hadoop-input/*  ~/hadoop-input/.



echo "This could take some time!"

cd raw

bunzip2 -k RC_2017-11.bz2

#mkdir -p ../data

mv RC_2017-11 ../../hadoop-input/.

#cd ../data/

#PWD=`pwd`
#echo $PWD

#cd ../../hadoop-input
#mv $PWD/RC_2017-11 .

ls -hal ../../hadoop-input/


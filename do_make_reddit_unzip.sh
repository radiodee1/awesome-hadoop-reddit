cd raw

bunzip2 -k RC_2017-11.bz2

mv RC_2017-11 ../data/.

cd ../data/

PWD=`pwd`
echo $PWD

cd ../../hadoop-input
ln -s $PWD/RC_2017-11 .

ls -hal


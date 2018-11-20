scrape reddit with hadoop

Note: 
The code in this folder uses hadoop streaming but also uses a python library called 'MRJob'. The complete code for this project can be found in the following github repository.

https://github.com/radiodee1/awesome-hadoop-reddit

You only need one python file if you want to test the MRJob functions. If you are looking at a zip file with only one python file, more code is found in the github directory. This extra code is not necessary for the project but shows the development of the files. You should install MRJob on your computer using pip3 if you want to test this code.

Instuctions - MRJob:

1. $ wget http://files.pushshift.io/reddit/comments/RC_2017-11.bz2
2. $ bunzip2 -k RC_2017-11.bz2
3. start hadoop
4. $ python3.6 job_test.py -r hadoop < RC_2017-11 > out.txt


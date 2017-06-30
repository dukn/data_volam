from os import listdir 
from os.path import isfile, join 
import os
os.system("ls -l")

cmd = ""

mypath = "../Data/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
for afile in onlyfiles:
	os.system("./vnTokenizer.sh -i ../Data/{} -o ../Data2/{}".format(afile,afile))

#print onlyfiles

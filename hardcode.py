from os import listdir 
from os.path import isfile, join 


mypath = "./Data2"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath,f))]
#print onlyfiles

out = open('dataTokenized.csv','w')
out.write("name,text\n")
for afile in onlyfiles:
	inp = open(mypath + "/" + afile).read() 
	aname = afile.split('.')[0]
	inp = inp.replace("\r\n"," ")
	inp = inp.replace("\n"," ")	
	inp = inp.replace(","," ")
	#print inp
	#break 
	out.write("{},{}\n".format(aname,inp))

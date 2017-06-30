import operator 
import datetime
import os 
import time 
from collections import OrderedDict
import math

import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.neighbors import NearestNeighbors

def time_diff_str(t1,t2):
	# Calculates time durations.
	diff = t2-t1
	mins = int(diff/60) 
	secs = round(diff%60,2)
	return str(mins) + " mins and " + str(secs) + " senonds"

def load_wiki_data(file_name):
	# Get reviews data, from local csv.
	if os.path.exists(file_name):
		print "--"+file_name + " round locally\n"
		df = pd.read_csv(file_name)
	return df 



# Define TF functions

def freq(word, doc):
	return doc.count(word)

def word_count(doc):
	return len(doc)

def tf(word,doc):
	return  (freq(word,doc)/ float(word_count(doc)))


# Denife IDF functions

def num_docs_containing(word, list_of_docs):
	count = 0 
	for document in list_of_docs:
		if freq(word,document) > 0 :
			count +=1 
	return 1 + count

def idf (word, list_of_docs):
	return math.log(len(list_of_docs)/float(num_docs_containing(word,list_of_docs)))

def tf_idf (word, doc, list_of_docs):
	return (tf(word,doc) * idf(word,list_of_docs))





people = load_wiki_data("dataTokenized.csv")

allsubject = []
for i in people["name"]:
	allsubject.append(i)
#print allsubject 
asubject = []
asubject_row_index = []
for _subject in allsubject:
	asubject.append(people[people["name"] == _subject])


print "---------------------------------"

tinyDict = open("tinyDict.txt",'w')

for _subject in asubject:
	_subject_dict = {}
	txt_subject = _subject["text"].tolist()[0]
	for word in txt_subject.split():
		a,b = word, tf(word,txt_subject)
		_subject_dict.update({a:b})
	# TF available
	
	_subject_dict2 = {}
	for word in txt_subject.split():
		a,b = word, tf_idf(word, txt_subject, people["text"])
		_subject_dict2.update({a:b}) 
	# TF IDF available 
	sorted_ = []
	sorted_ = sorted(_subject_dict2.items(), key=operator.itemgetter(1))
	#print sorted_
	for i in range(len(sorted_)-1,10,-1):
		ii = sorted_[i]
		if round(100.*ii[1],2) > 0.03 and len(ii[0]) > 4:
			print ii[0], round(100.*ii[1],2)
			tinyDict.write(ii[0])
			tinyDict.write("\n")


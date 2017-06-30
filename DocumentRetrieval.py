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

people = load_wiki_data("dataTokenized.csv")
#print people.head()
#print len(people)

# Print a record.
if 1:
	banghoi = people[people["name"]=="banghoi"]
	banghoi_row_index = banghoi.index.tolist()[0]
	print "banghoi:", banghoi

# Define TF functions

def freq(word, doc):
	return doc.count(word)

def word_count(doc):
	return len(doc)

def tf(word,doc):
	return  (freq(word,doc)/ float(word_count(doc)))

print "---------------------------------"
# Calculate term frequncy
banghoi_dict = {}
txt_banghoi = banghoi["text"].tolist()[0]

print "-- banghoi term frequence"
for word in txt_banghoi.split():
	a,b = word, tf(word,txt_banghoi) 
	#print a,b
	banghoi_dict.update({a:b})

if False:
	sorted_ = sorted(banghoi_dict.items(), key=operator.itemgetter(1))
	#print sorted_
	for i in range(len(sorted_)-1,10,-1):
		ii = sorted_[i]
		print ii[0], round(ii[1],5)

#sorted_by_value = OrderedDict(sorted(banghoi_dict.items(), key=lambda x: x[1]))
#print sorted_by_value

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


print "********************"

dict2  = {}

for word in txt_banghoi.split():
	a,b = word, tf_idf(word,txt_banghoi, people["text"])
	dict2.update({a:b})


if True:
	sorted_ = sorted(dict2.items(), key=operator.itemgetter(1))
	#print sorted_
	for i in range(len(sorted_)-1,10,-1):
		ii = sorted_[i]
		print ii[0], round(100.*ii[1],2)


import codecs
import re
import nltk
import os
from sklearn.metrics import accuracy_score
import gensim.models.word2vec as w2v
import sklearn.manifold
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC


file = codecs.open("parsed.txt","r","utf-8")
lines = file.read()
lines = lines.split("\n")
from random import shuffle
shuffle(lines)
def wordlist(raw):
	raw = raw.lower()
	clean = re.sub("[^a-zA-Z]"," ", raw)
	words = clean.split()
	return words

for index, item in enumerate(lines):
	item = wordlist(item)
	lines[index] = item


emotion=[]
for sent in lines:
	if (len(sent))==0:
		continue
	emotion.append(sent.pop(0)) 


le = LabelEncoder()
le.fit(['joy','anger','sadness','fear'])
emotion = le.transform (emotion)
print(len(emotion))
thrones2vec = w2v.Word2Vec.load(os.path.join("trained", "thrones2vec.w2v"))

sentence_vectors = []

for sentence in lines:
	sentence_vectors.append(np.mean([thrones2vec.wv[words] for words in sentence if words in thrones2vec] or [np.zeros(300)],axis=0))


clf = LinearSVC()
train = sentence_vectors[:800]
trainlabel = emotion[:800]
test = sentence_vectors[800:]
testlabel = emotion[800:]


clf.fit(train,trainlabel)



sente = 'The rain is so beautiful'.split()

vector = np.mean([thrones2vec.wv[words] for words in sente if words in thrones2vec] or [np.zeros(300)],axis=0)

newlist = ['1']
newlist[0] = vector

predict = clf.predict(test)
error = 0
print(vector)
for i in range(0,len(predict)):
	if(predict[i]!=testlabel[i]):
		error = error+1

print(error)






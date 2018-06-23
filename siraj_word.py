import codecs 
import glob
import logging 
import multiprocessing
import os
import pprint 
import re


import nltk
import gensim.models.word2vec as w2v
import sklearn.manifold
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#    np.mean([word2vec[w] * tfidf[w] for w in words if w in word2vec] or [np.zeros(dim)], axis=0)


# #%pylab inline

# corpus_raw = u""

# filelist = ['got1.txt','got2.txt','got3.txt','got4.txt','got5.txt']
# for file in filelist:
# 	with codecs.open(file,"r","utf-8")as book_file:
# 		corpus_raw +=  book_file.read()

# print ("Corpus is now",len(corpus_raw), "long")



# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# raw_sentences = tokenizer.tokenize(corpus_raw)

# def sentence_to_wordlist(raw):
#     clean = re.sub("[^a-zA-Z]"," ", raw)
#     words = clean.split()

#     return words
# sentance = []

# for element in raw_sentences:
# 	if (len(element))>0:
# 		sentance.append(sentence_to_wordlist(element))


# for sent in sentance:
# 	for i in range(len(sent)):
# 			sent[i] = sent[i].lower()
# print (sentance)


# token_count = sum([len(sent) for sent in sentance])
# print("--------------",token_count)


# num_features = 300
# min_word_count = 3
# num_workers = multiprocessing.cpu_count()
# context_size = 7
# downsampling = 1e-3
# seed = 1


# thrones2vec = w2v.Word2Vec(
#     sg=1,
#     seed=seed,
#     workers=num_workers,
#     size=num_features,
#     min_count=min_word_count,
#     window=context_size,
#     sample=downsampling
# )
# thrones2vec.build_vocab(sentance)
# thrones2vec.train(sentance, total_words=token_count, epochs=100)

# print("Word2Vec vocabulary length:", len(thrones2vec.wv.vocab))

# if not os.path.exists("trained"):
#     os.makedirs("trained")
# thrones2vec.save(os.path.join("trained", "thrones2vec.w2v"))







thrones2vec = w2v.Word2Vec.load(os.path.join("trained", "thrones2vec.w2v"))
print(thrones2vec.most_similar(positive=['king','girl'],negative=['boy']))
print(thrones2vec.most_similar("girl"))
print(thrones2vec.wv.doesnt_match('boy girl king queen'.split()))

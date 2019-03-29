#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:25:36 2019

@author: ivetaskorpilova
"""

import nltk



### stop slova v anglictine
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

### nacteni souboru s recenzemi
f = open('reviews.txt')
text = f.read().lower()

### rozdeleni recenzi na jednotliva slova
from nltk.tokenize import word_tokenize
tokenized_text=word_tokenize(text)
#print(tokenized_text) # vypsani recenzi rozdelenych na jednotliva slova

filtered_sentence = []
#
#### seznam specialnich symbolu, ktere chceme vyfiltrovat
import string
symbols = list(string.punctuation)
#
#### seznam vlastnich slov, ktera chceme vyfiltrovat
own = ["The","...", "I", "It"]


#lemmatization
from nltk.stem.wordnet import WordNetLemmatizer
lem = WordNetLemmatizer()    

#
#### vyfiltrovani stopslov
stop = stop_words + symbols + own
for w in tokenized_text: 
    if w not in stop: 
      filtered_sentence.append(lem.lemmatize(w,"v")) 
       
      

#určení slovních druhů           
tagged=nltk.pos_tag(filtered_sentence) 
  
#ponechání pouze NN RB
fil_tagged = [t for t in tagged if (t[1] == "NN") or (t[1] =="RB")]
#print(fil_tagged)  




#import sjednocení slov se stejným kořenem
#from nltk.stem import PorterStemmer
#ps = PorterStemmer()
#ps.stem(w)

# seznam slov v recenzich
#print(len(filtered_sentence))  # pocet slov v recenzich
###
##### vytovreni slovniku s frekvencemi jednotlivych slov v recenzich
#from nltk.probability import FreqDist
#fdist = FreqDist(filtered_sentence)
#print(fdist.most_common(len(filtered_sentence)))  # vypis slov a jejich frekvenci
#
##
#### vytvoreni bigramu a jejich frekvenci
#bgs = nltk.bigrams(filtered_sentence)
#fdist = nltk.FreqDist(bgs)
#print(fdist.most_common(len(filtered_sentence)))  # vypis bigramu a jejich frekvenci
#

##sorte_d = sorted(fdist.items(), key=lambda(k,v): v)
# 	
#sorted_d = sorted((value, key) for (key,value) in fdist.items())
#
#for k,v in sorted_d:
#    print (k,v)

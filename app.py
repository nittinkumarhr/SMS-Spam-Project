import streamlit as st
import pandas as pd
import pickle
import sklearn
import nltk
import string
from sklearn import preprocessing

from nltk.stem.porter import PorterStemmer


# ps=PorterStemmer()
# def transform_Text(text):
#     text = text.lower()
#     text = nltk.word_tokenize(text)
#     y=[]  
#     for i in text:
#         if i.isalnum():
#             y.append(i)
#     text=y[:]
#     y.clear()
#     for i in text:
#         if i not in stopwords.words('english') and i not in string.punctuation:
#             y.append(i)
#     #NOTE - =================
#     text = y[:]
#     y.clear()
#     for i in text:
#         y.append(ps.stem(i))
#     return " ".join(y)

tfidf=pickle.load(open('/home/nitin/Documents/tfidf.pickle','rb'))
model=pickle.load(open('/home/nitin/Documents/model.pickle','rb'))


st.title("Email Spam Classifier")
input_sms=st.text_input("Enter the Message")

#1 preprocess

# 2Vectorize
#.3 predict
# 4 Display


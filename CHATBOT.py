#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
import io
import numpy as np
import random
import string
import warnings
warnings.filterwarnings('ignore')


# In[2]:


f=open('globalwarming.txt','r',errors='ignore')
raw= f.read()
raw=raw.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens=nltk.sent_tokenize(raw)
word_tokens=nltk.word_tokenize(raw)


# In[3]:


sent_tokens[:2]


# In[4]:

# converts the tokens into sentences
word_tokens[:2]

# converts the tokens to words
# In[5]:


lemmer= nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return[lemmer.lemmatize(token) for token in tokens]
remove_punct_dict= dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


# In[6]:


GREETING_INPUTS = ('hello','hi','greeting','sup','what is up', 'hey')
GREETING_RESPONSES= ['hi','hey','nods','hi there','hello','I am glad that you are talking to me']
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# In[7]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[8]:


from sklearn.metrics.pairwise import cosine_similarity


# In[9]:


def response (user_response):
    chatbot_response=''
    sent_tokens.append(user_response)
    TfidfVec= TfidfVectorizer(tokenizer=LemNormalize,stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals=cosine_similarity(tfidf[-1],tfidf)
    idx=vals.argsort()[0][-2]
    flat= vals.flatten()
    flat.sort()
    req_tfidf= flat[-2]
    if (req_tfidf==0):
        chatbot_response=chatbot_response+'I am sorry. I do not understand you'
        return chatbot_response
    else:
        chatbot_response= chatbot_response+sent_tokens[idx]
        return chatbot_response


# In[ ]:


flag = True
print('Chatbot: My name is jenny. I will answer your questions about global warming. If you wanna exit, type bye')
while(flag==True):
    user_response= input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if (user_response=='thanks' or user_response=='thank you'):
            flag= False
            print('Chatbot:You are welcome..')
        else:
            if(greeting(user_response)!=None):
                print('Chatbot:'+greeting(user_response))
            else:
                print('Chatbot:', end='')
                print(response(user_response))
                sent_tokens.remove(user_response)
                
                
                
                
                
    else:
        flag= False
        print("Chatbot: Bye! Take care.")


# In[ ]:





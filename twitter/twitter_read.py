#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
from tweepy import OAuthHandler, Stream


# In[2]:


from tweepy.streaming import StreamListener
import socket
import json
from django.core.exceptions import ImproperlyConfigured
import os
from pathlib import Path


# configuration for secret key in order to hide at git server

# In[3]:


secret_file = os.path.join(os.getcwd(), 'secret.json')

with open(secret_file) as f:
    key = json.loads(f.read())

def get_secret(setting, key=key):
    try:
        return key[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

consumer_key = get_secret("CONSUMER_KEY")
consumer_secret = get_secret("CONSUMER_SECRET")
access_token = get_secret("ACCESS_TOKEN")
access_secret = get_secret("ACCESS_SECRET")


# In[4]:


class TweetListener(StreamListener):
    
    def __init__(self, csocket):
        self.client_socket = csocket
        
    def on_data(self, data):
        try:
            msg = json.loads(data)
            print(msg['text'].encode('utf-8'))
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("ERROR ", e)
            return True
        
    def on_error(self, status):
        print(status)
        return True


# In[5]:


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    twitter_stream = Stream(auth, TweetListener(c_socket))
    twiiter_stream = filter(track=['guiter'])


# In[ ]:


if __name__ == "__main__":
    s = socket.socket()
    host = '127.0.0.1'
    port = 5555
    s.bind((host, port))
    
    print(f'listenning on port {port}')
    
    s.listen(5)
    c, addr = s.accept()
    
    sendData(c)


# In[ ]:





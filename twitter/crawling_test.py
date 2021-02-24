import tweepy
from tweepy.streaming import StreamListener
import socket
import json
import os
from pathlib import Path
import pandas as pd
import time

secret_file = os.path.join(os.getcwd(), 'secret.json')

with open(secret_file) as f:
    key = json.loads(f.read())


def get_secret(setting, key=key):
    try:
        return key[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise print(error_msg)


consumer_key = get_secret("CONSUMER_KEY")
consumer_secret = get_secret("CONSUMER_SECRET")
access_token = get_secret("ACCESS_TOKEN")
access_secret = get_secret("ACCESS_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

text_query="tiger woods"
count = 20
try:
    tweets = tweepy.Cursor(api.search, q=text_query).items(count)
    tweets_list = [[f"{tweet.text}\n" ] for tweet in tweets]
    print(tweets_list)
    tweets_df = pd.DataFrame(tweets_list)
    print(tweets_df)
except BaseException as e:
    print('failed on_status', str(e))
    time.sleep(3)

# Reference : https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1
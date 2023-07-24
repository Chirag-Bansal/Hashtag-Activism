import datetime
import time
from pytz import utc
import tweepy
import configparser
import pandas as pd
import matplotlib.pyplot as plt
import csv  
import numpy as np

header = ['SNo','id','text','retweet_count','reply_count','like_count','quote_count','possibly_sensitive','author_id','date','lang','hashtags','link']

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

bearer_token = config['twitter']['bearer_token']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

client_ID = config['twitter']['client_ID']
client_secret = config['twitter']['client_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token)#,wait_on_rate_limit =True)

# function to display data of each tweet
def printtweetdata(n, ith_tweet):
        print()
        print(f"Tweet {n}:")
        print(f"Username:{ith_tweet[0]}")
        print(f"Location:{ith_tweet[1]}")
        print(f"Following Count:{ith_tweet[2]}")
        print(f"Follower Count:{ith_tweet[3]}")
        print(f"Total Tweets:{ith_tweet[4]}")
        print(f"Retweet Count:{ith_tweet[5]}")
        print(f"Tweet Text:{ith_tweet[6]}")
        print(f"Hashtags Used:{ith_tweet[7]}")

# function to perform data extraction
def search(hashtag,filename,numtweets):
        
        query = hashtag +' is:retweet'
        # Replace with time period of your choice
        start_date = input("Enter Start Date in YYYY-MM-DD format: ")
        start_time = start_date + 'T00:00:00Z'
        # Replace with time period of your choice
        end_date = input("Enter End Date in YYYY-MM-DD format: ")
        end_time = end_date + 'T00:00:00Z'

        f = open(filename, 'a', encoding="utf-8")
        writer = csv.writer(f)
        writer.writerow(header)
          
        i = 1
        response = client.search_all_tweets(query=query,
                                        tweet_fields=['attachments', 'author_id','conversation_id', 'created_at','edit_controls', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang',
                                                        'public_metrics', 'possibly_sensitive', 'referenced_tweets', 'reply_settings', 'source', 'text', 'withheld'],
                                        user_fields= ['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected','public_metrics', 'url', 'username', 'verified', 'withheld'],
                                        expansions = ['attachments.poll_ids', 'attachments.media_keys', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'referenced_tweets.id', 'referenced_tweets.id.author_id'],
                                        start_time=start_time,
                                        end_time=end_time,
                                        # next_token = 'b26v89c19zqg8o3fos8t7ewbc4m96jsiv8q59mj0cz2il',
                                        # next_token = '1jzu9lk96gu5npw44wer7pvouhvg424i6rkcf1o8qp31',
                                        max_results = numtweets)
        list_tweets = [tweet for tweet in response.data]
        next_token = response.meta.get('next_token')
        print(next_token)
        first = True
        for tweet in list_tweets:
                id = tweet.id
                text = tweet.text
                retweet_count = tweet.public_metrics['retweet_count']
                reply_count = tweet.public_metrics['reply_count']
                like_count = tweet.public_metrics['like_count']
                quote_count = tweet.public_metrics['quote_count']
                possibly_sensitive = tweet.possibly_sensitive
                author_id = tweet.author_id
                date = tweet.created_at
                lang = tweet.lang
                if tweet.entities is not None and tweet.entities.get('hashtags') is not None:
                        tags = [hash['tag'] for hash in tweet.entities.get('hashtags')]
                else:
                        tags = []
                link = 'https://twitter.com/edent/status/' + str(id)

                ith_tweet = [i,id,text, retweet_count,reply_count,like_count,quote_count,possibly_sensitive,author_id,date,lang,tags,link]
                if first:
                        print(ith_tweet)
                        first = False
                writer.writerow(ith_tweet)
                i += 1
        print(i)
        time.sleep(2)
        while next_token:
                response = client.search_all_tweets(query=query,
                                        tweet_fields=['attachments', 'author_id', 'conversation_id', 'created_at','edit_controls', 'entities', 'geo', 'id', 'in_reply_to_user_id', 'lang',
                                                        'public_metrics', 'possibly_sensitive', 'referenced_tweets', 'reply_settings', 'source', 'text', 'withheld'],
                                        user_fields= ['created_at', 'description', 'entities', 'id', 'location', 'name', 'pinned_tweet_id', 'profile_image_url', 'protected','public_metrics', 'url', 'username', 'verified', 'withheld'],
                                        expansions = ['attachments.poll_ids', 'attachments.media_keys', 'author_id', 'edit_history_tweet_ids', 'entities.mentions.username', 'geo.place_id', 'in_reply_to_user_id', 'referenced_tweets.id', 'referenced_tweets.id.author_id'],
                                        start_time=start_time,
                                        end_time=end_time, 
                                        next_token = next_token,
                                        max_results = numtweets)
                if response.data is None:
                        break
                list_tweets = [tweet for tweet in response.data]
                next_token = response.meta.get('next_token')
                print(next_token)
                # print(response.meta)
                for tweet in list_tweets:
                        id = tweet.id
                        text = tweet.text
                        retweet_count = tweet.public_metrics['retweet_count']
                        reply_count = tweet.public_metrics['reply_count']
                        like_count = tweet.public_metrics['like_count']
                        quote_count = tweet.public_metrics['quote_count']
                        possibly_sensitive = tweet.possibly_sensitive
                        author_id = tweet.author_id
                        date = tweet.created_at
                        lang = tweet.lang
                        if tweet.entities is not None and tweet.entities.get('hashtags') is not None:
                                tags = [hash['tag'] for hash in tweet.entities.get('hashtags')]
                        link = 'https://twitter.com/edent/status/' + str(id)

                        ith_tweet = [i,id,text, retweet_count,reply_count,like_count,quote_count,possibly_sensitive,author_id,date,lang,tags,link]
                        writer.writerow(ith_tweet)
                        i += 1
                print(i)
                time.sleep(2)
        
def username(user_id_list):
        for user_id in user_id_list:
                user = api.get_user(user_id=user_id)
                screen_name = user.screen_name
                print(screen_name)





numtweet = 100
hashtag = input("Enter tweet query like #hathras OR #justiceforasifa :")
search(hashtag,"retweet.csv", numtweet)

from operator import itemgetter
import pandas as pd

file = input("Input File Name: ")
words = dict()
df = pd.read_csv("Data" + '/' + file +'.csv')

RT_per_author = dict()
tweets_per_author = dict()

for ind,row in df.iterrows():
    try:
        if row['Author Id'] in RT_per_author:
            RT_per_author[str(row['Author Id'])] += row['Retweet Count']
            tweets_per_author[str(row['Author Id'])] += 1
        else:
            RT_per_author[str(row['Author Id'])] = row['Retweet Count']
            tweets_per_author[str(row['Author Id'])] = 1
    except:
        continue

top_authors = sorted(RT_per_author, key=RT_per_author.get, reverse=True)

top_tweet_authors = sorted(tweets_per_author, key=tweets_per_author.get, reverse=True)

print(top_authors)
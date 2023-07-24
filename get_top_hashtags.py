from operator import itemgetter
import pandas as pd

file = input("Input File Name: ")
hashtags = dict()
df = pd.read_csv("Data" + '/' + file +'.csv')
print(len(df))
for i in range(len(df)):
    for hashtag in df.iloc[i][11].strip('][').split(', '):
        hashtag = hashtag.lower()
        if hashtag in hashtags:
            hashtags[hashtag] += 1
        else:
            hashtags[hashtag] = 1

N = int(input("Enter Number of Hashtags Needed: "))
res = dict(sorted(hashtags.items(), key = itemgetter(1), reverse = True)[:N])

for key in res:
  print([key, res[key]])
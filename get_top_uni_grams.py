from operator import itemgetter
import pandas as pd

file = input("Input File Name: ")
words = dict()
df = pd.read_csv("Data" + '/' + file +'.csv')
for i in range(len(df)):
    for word in df.iloc[i][2].split(' '):
      word = word.lower()
      if word in words:
        words[word] += 1
      else:
        words[word] = 1

N = int(input("Enter Number of Unigrams Needed: "))
res = dict(sorted(words.items(), key = itemgetter(1), reverse = True)[:N])

for key in res:
  print([key, res[key]])
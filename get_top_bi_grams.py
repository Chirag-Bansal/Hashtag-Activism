from operator import itemgetter
import pandas as pd

file = input("Input File Name: ")
bi_gram_words = dict()
df = pd.read_csv("Data" + '/' + file +'.csv')
for i in range(len(df)):
    word = df.iloc[i][2].split(' ')
    for j in range(len(word)-1):
      word[j] = word[j].lower()
      word[j+1] = word[j+1].lower()
      bi_gram = word[j] + " " + word[j+1]
      if bi_gram in bi_gram_words:
        bi_gram_words[bi_gram] += 1
      else:
        bi_gram_words[bi_gram] = 1

N = int(input("Enter Number of Bigrams Needed: "))
res = dict(sorted(bi_gram_words.items(), key = itemgetter(1), reverse = True)[:N])

for key in res:
  print([key, res[key]])
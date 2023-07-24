from operator import itemgetter
import pandas as pd

file = input("Input File Name: ")
tri_gram_words = dict()
df = pd.read_csv("Data" + '/' + file +'.csv')
for i in range(len(df)):
    word = df.iloc[i][2].split(' ')
    for j in range(len(word)-2):
      word[j] = word[j].lower()
      word[j+1] = word[j+1].lower()
      word[j+2] = word[j+2].lower()
      tri_gram = word[j] + " " + word[j+1] + " " + word[j+2]
      if tri_gram in tri_gram_words:
        tri_gram_words[tri_gram] += 1
      else:
        tri_gram_words[tri_gram] = 1

N = int(input("Enter Number of Trigrams Needed: "))
res = dict(sorted(tri_gram_words.items(), key = itemgetter(1), reverse = True)[:N])

for key in res:
  print([key, res[key]])
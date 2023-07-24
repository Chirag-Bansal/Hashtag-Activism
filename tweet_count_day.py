from operator import itemgetter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

file = input("Input File Name: ")
words = dict()
columns = ['Serial Number', 'Tweet ID','Text of tweet', 'Retweet Count', 'Reply Count', 'Like Count', 'Quote Count', 'Senitivity', 'Author Id', 'Date', 'Language', 'Hashtags','Link of the tweet']
df = pd.read_csv("Data" + '/' + file +'.csv', encoding='utf-8', encoding_errors='ignore', names=columns)

monthCount = dict()
dayCount = dict()

data_issues = 0
for date in df['Date']:
  if not isinstance(date, str):
    data_issues += 1
    continue 
  if date[0:7] in monthCount:
    monthCount[date[0:7]] +=1
  else:
    monthCount[date[0:7]] =1
  if date[0:10] in dayCount:
    dayCount[date[0:10]] +=1
  else:
    dayCount[date[0:10]] =1

for day in list(dayCount):
  if '[' in day:
    del dayCount[day]

for month in list(monthCount):
  if '[' in month:
    del monthCount[month]

myKeys = list(dayCount.keys())
myKeys.sort()
dayCount = {i: dayCount[i] for i in myKeys}

month = input("Enter Month in YYYY-MM format: ")
y_values = []
text_values = []
for day in list(dayCount):
  if month not in day:
    continue
  text_values.append(day)
  y_values.append(dayCount[day])

x_values = np.arange(1, len(text_values) + 1, 1)

plt.bar(x_values, y_values, align='center')
plt.xticks(x_values, text_values)
plt.gcf().set_size_inches(45,8)
plt.tight_layout()
plt.savefig(month + '.png')
plt.show()
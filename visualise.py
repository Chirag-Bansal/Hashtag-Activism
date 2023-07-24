import matplotlib.pyplot as plt
import numpy as np

def visualise(hashtag):
        with open('#' + hashtag+ '.txt', 'r') as f:
                Lines = f.readlines()
                y = [int(line) for line in Lines]

        y2 = y.copy()

        for i in range(1,len(y)):
                y2[i] -= y[i-1]

        x = np.arange(1, len(y2)+1)
        # plotting
        plt.title("Tweets on that day")
        plt.xlabel("Days")
        plt.ylabel("Total Tweets")
        plt.plot(x, y2, color ="green")
        plt.savefig(hashtag+'.png')

hashtag = input("Enter hashtag :")
vis = input("Input YES to visualise daily tweet count else press enter :")
if vis == "YES":
        visualise(hashtag)

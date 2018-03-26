import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

f = open('euro_sentiment.txt', 'r')
euro_f = f.read().splitlines()

f2 = open('usa_sentiment.txt', 'r')
usa_f = f2.read().splitlines()

euro = []
usa = []

for i in range(0,110):
    euro.append(float(euro_f[i]))
    usa.append(float(usa_f[i]))

# EU values
N = 110
euro_mean = np.mean(euro)
euro_var = sum([pow(e - euro_mean, 2) for e in euro]) / (N - 1)

# US values
usa_mean = np.mean(usa)
usa_var = sum([pow(u - usa_mean, 2) for u in usa]) / (N - 1)

# t-statistic
t = (euro_mean - euro_mean) / np.sqrt((euro_var/N) + (usa_var/N))

# g
# r
# a
# p
# h

bins = [-1, -.9, -.8, -.7, -.6, -.5, -.4, -.2, -.1, 0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1]

plt.figure().patch.set_facecolor('#404040')
plt.hist(euro, bins, alpha=0.6, edgecolor='black', linewidth=.8)
plt.hist(usa, bins, alpha=0.5, edgecolor='black', linewidth=.8)

ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
ax.set_facecolor('#404040')

# line = mlab.normpdf(bins, euro_mean, np.sqrt(euro_var))
# plt.plot(bins, line, 'r--')

plt.xlabel('Sentiment Value Clusters', fontsize=13)
plt.ylabel('Count', fontsize=13)
plt.title('Sentiment Values for EU & US News Articles', fontsize=16)
plt.legend()
plt.show()

# print("t statistic:", t)
# print("scipy t stat:", stats.ttest_ind(euro, usa).statistic)
# print('euro variance: ', usa_var)
# print('usa variance: ', usa_var)


# print('numpy:       ', np.var(usa))
# print("euro: ", euro)
# print("---------------------------------------------------------------------------------------------------------------------------------------")
# print("usa: ", usa)

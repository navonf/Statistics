import pandas as pd
import numpy as np

f = open('euro_sentiment.txt', 'r')
euro_f = f.read().splitlines()

f2 = open('usa_sentiment.txt', 'r')
usa_f = f2.read().splitlines()

euro = []
usa = []
for i in range(0,110):
    euro.append(float(euro_f[i]))
    usa.append(float(usa_f[i]))

N = 110
euro_mean = np.mean(euro)
euro_var = sum([pow(e - euro_mean, 2) for e in euro]) / (N - 1)

usa_mean = np.mean(usa)
usa_var = sum([pow(u - usa_mean, 2) for u in usa]) / (N - 1)
# print('euro variance: ', usa_var)
print('usa variance:  ', usa_var)


# print('numpy:       ', np.var(usa))
# print("euro: ", euro)
# print("---------------------------------------------------------------------------------------------------------------------------------------")
# print("usa: ", usa)

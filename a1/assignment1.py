import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Students's t-test
# large t-score, bigger difference between groups
# small t-score, more similarity between groups

# null hypothesis: the fish belong to the same species in the catalogue.
# alternative hyp: the fish do not belong to the same species in the catalogue.
# W = [1.25, 2, 1.75, 1, 1.3, 1.8, 1.7, 1.2, 1.5]
# t = stats.ttest_1samp(W, 1.65)
# print(t)

# y axis Sq dependent, x axis T independent
# T = [52,52,50,54,50,52,54,80,80]
# Sq = [8,10,6,9,6,12,12,1,0]
# N = 9
# xy, x_2, y_2 = 0, 0, 0
# # work for intercept and slope:
# for i in range(0, len(T)):
#     xy += T[i] * Sq[i]
#     x_2 += pow(T[i], 2)
#     y_2 += pow(Sq[i], 2)
#
# slope = ((N * xy) - (sum(T) * sum(Sq))) / ((N * x_2) - pow(sum(T), 2))
# inter = ((sum(Sq) * x_2) - (sum(T) * xy)) / ((N * x_2) - pow(sum(T), 2))
#
# print("Slope =", slope)
# print("Intercept =", inter)
# data_one_month = pd.read_csv('coindesk-USD-BTC-data-2018-01-24_2018-02-08.csv', header=None)
# data_two_year = pd.read_csv('coindesk-USD-BTC-data-2016-02-07_2018-02-08.csv', header=None)
#
# mean_two_year = data_two_year[1].mean()
# one_sample = stats.ttest_1samp(data_one_month, mean_two_year)
# print(one_sample)

# H = [3,4,9,10,6,7]
# E = [80, 90, 75, 95, 85, 85]
# slope, intercept, r_value, p_value, std_err = stats.linregress(H, E)
# print("p value =", p_value)
# plt.plot(H, E, 'o', label='original data')
# plt.plot(np.unique(H), np.poly1d(np.polyfit(H, E, 1))(np.unique(H)), label='fitted line')
# plt.legend()
# plt.show()

# F test
# H = [3,4,9,10,6,7]
# E = [80, 90, 75, 95, 85, 85]
# N = 6
# k = 1 # one input parameter, horoscope score
# XY = sum([H[i] * E[i] for i in range(0, N)])
# SSXY = XY - ((sum(H) * sum(E)) / N)
# SSX = sum([i * i for i in H])
# SSXX = SSX - (pow(sum(H), 2) / N)
# beta1 = SSXY/SSXX
# SSY = sum([i * i for i in E])
# SSYY = SSY - (pow(sum(E), 2)/N)
# SSE = SSYY - (beta1 * SSXY)
# # our final F equation
# F = ((SSY - SSE) / k) / (SSE / (N - k - 1))
# print("F =", round(F, 3))

# regression line for ad budget spending
# x = np.random.random(10)
# y = np.random.random(10)
# slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
# plt.plot(x, y, 'o', label='original data')
# plt.plot(x, intercept + slope*x, 'r', label='fitted line')
# plt.legend()
# plt.show()

# GDP affected by population
pop = [324532000, 144554993, 60674003, 92700000, 31151643, 4757967]
gdp = [57294, 25185, 36191, 6377, 13018, 69375]
labels = ["USA", "Russia", "Italy", "Vietnam", "Peru", "Ireland"]
slope, intercept, r_value, p_value, std_err = stats.linregress(pop, gdp)
print("p value =", p_value)
plt.plot(pop, gdp, 'o', label='original data')
plt.plot(np.unique(pop), np.poly1d(np.polyfit(pop, gdp, 1))(np.unique(pop)), label='fitted line')
plt.legend()
for i in range(0, len(pop)):
    plt.annotate(
        labels[i],
        xy=(pop[i], gdp[i]), xytext=(40, 10),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
plt.show()

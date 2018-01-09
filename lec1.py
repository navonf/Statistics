import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Two way table.
aa = np.array(['red','green', 'green', 'green', 'red', 'red'])
bb = np.array(['spring', 'spring', 'summer', 'summer', 'summer', 'autumn'])
ct = pd.crosstab(aa, bb, rownames=['snakeColor'], colnames=['seasonName'])

print(ct)

ct.plot(style='o', fontsize=18, markersize=22)
plt.show()

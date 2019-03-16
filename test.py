

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


incomes = np.random.normal(27000, 15000, 10000)
ages = np.random.randint(10,high=90,size=500)

print(ages)
print(np.median(incomes))

plt.hist(incomes, 50)
plt.show()

print(stats.mode(ages))


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

rnd_arr = np.random.randint(0, 10, 100).reshape(2, 50)
fig, ax = plt.subplots(1, 2, figsize = (50, 5))
ax[0].hist(rnd_arr[0], color='g', label = 'First 50')
ax[1].hist(rnd_arr[1], color='b', label = 'last50')
ax[0].legend()
ax[1].legend()

plt.show()
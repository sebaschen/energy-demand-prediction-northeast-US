import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./data/PJME_hourly.csv')

x,y = df["Datetime"][:300],df["PJME_MW"][:300]

plt.plot(x,y)
plt.show()


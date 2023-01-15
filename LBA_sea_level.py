# LBA sea level assignment

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('LBA_NS - Sheet1 (4).csv')
billion_lst = df['Billions'].tolist()
billion = [int(item) for item in billion_lst]
year = df['Year'].tolist()

plt.plot(df['Year'], billion)
plt.xticks(rotation=90)
plt.xticks(year)
#plt.locator_params(axis="x", tight=False, nbins=16)
plt.title('Tourist generated venue every year (1999-2021)')
plt.xlabel('Year')
plt.ylabel('Venue in Billions (US Dollars)')
plt.show()












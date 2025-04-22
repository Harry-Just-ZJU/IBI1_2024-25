import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# TASK 1
os.chdir('C:/Users/yxhua/Desktop/IBI/IBI1_2024-25/IBI1_2024-25/Practical10')

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

'''
print(dalys_data.head(5))
print(dalys_data.info()) 

print(dalys_data.describe()['DALYs']['max'])
print(dalys_data.describe()['DALYs']['min'])

print(int(dalys_data.describe()['Year']['max']))
print(int(dalys_data.describe()['Year']['min']))

print(dalys_data.iloc[0,3])

print(dalys_data.iloc[2,0:5])
print(dalys_data.iloc[0:2,:])
print(dalys_data.iloc[0:10:2,0:5])

print(dalys_data.iloc[0:3,[0,1,3]])

my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3,my_columns])

print(dalys_data.loc[2:4,"Year"])
'''


# TASK 2
print(dalys_data.iloc[0:10, 2])
print('the 10th year with DALYs data recorded in Afghanistan:', dalys_data.iloc[9, 2])

# TASK 3
print(dalys_data.loc[dalys_data['Year'] == 1990, "DALYs"])

# TASK 4

uk = dalys_data.loc[dalys_data['Entity'] == 'United Kingdom', ['DALYs', 'Year']]
fr = dalys_data.loc[dalys_data['Entity'] == 'France', ['DALYs', 'Year']]

uk_mean = uk['DALYs'].mean()
fr_mean = fr['DALYs'].mean()

if uk_mean > fr_mean:
    print('The mean DALYs in the UK was greater than France.')
elif uk_mean < fr_mean:
    print('The mean DALYs in the UK was smaller than France.')
else:
    print('The mean DALYs in the UK was equall to France.')

# TASK 5
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.xticks(uk.Year,rotation=-90)
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYS over time in the UK')
plt.show()


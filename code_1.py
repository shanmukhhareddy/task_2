import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("Sample - Superstore.csv",delimiter=",",encoding='windows-1252')
print(data)
plt.hist(data["Country"])
data.drop_duplicates()
cat_data=data['Category'].unique()

for i in range(3):
    data['Category']=np.where(data['Category']==cat_data[i],i,data['Category'])
reg=data['Region'].unique()

for i in range(4):
    data['Region']=np.where(data['Region']==reg[i],i,data['Region'])
data['Region']

data=data.drop('Product Name',axis=1)

np.savetxt('Final_data.csv',data,fmt = '%s',delimiter=',')

print(plt.hist(data["Country"]))